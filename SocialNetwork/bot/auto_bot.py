import os
import sys
import json
import random
import string
import clearbit
import logging

from django.conf import settings
from django.db.models import Count, Max, Q
from collections import namedtuple
from rest_framework.test import APIClient
from concurrent.futures import ThreadPoolExecutor

from authentication.models import User
from post.models import Post
from post.views import PostViewSet, PostLikeViewSet

clearbit.key = settings.CLEARBIT_API_KEY
log = logging.getLogger(__name__)


class BotConfig:

    client = APIClient()

    def __init__(self, *args, **kwargs):
        # Loading config.json
        try:
            with open(os.path.join(settings.BASE_DIR,
                                   'config.json')) as config_file:
                config_data = json.loads(config_file.read())
                bot_config = namedtuple('BotConfig', config_data.keys())
                self.config = bot_config(*config_data.values())
        except Exception as e:
            log.exception(e)

    def _generate_random_post(self, user):
        try:
            posts = Post.objects.annotate(total_likes=Count('likes')).filter(
                ~Q(owner=user), total_likes=0)[:self.config.max_likes_per_user]
            if not posts:
                raise StopIteration('No post found with 0 likes')
            yield random.choice(posts)
        except Exception as e:
            log.exception(e)

    def _perform_signup(self, email):
        try:
            self.client.post(
                '/auth/signup/', {
                    'email': email,
                    'password': 'password'
                },
                format='json')
        except Exception as e:
            log.exception(e)

    def _create_random_post(self, email):
        try:
            user = User.objects.get(email=email)
            while user.posts.count() <= self.config.max_posts_per_user:
                key = ''.join([
                    random.choice(string.ascii_uppercase + string.digits)
                    for _ in range(5)
                ])
                value = ''.join([
                    random.choice(string.ascii_uppercase + string.digits)
                    for _ in range(5)
                ])
                post_payload = {"post": {key: value}}
                self.client.login(email=email, password='password')
                log.info("User %s is creating post %s" % (email, post_payload))
                response = self.client.post(
                    '/posts/', post_payload, format='json')
            else:
                self.client.logout()
        except Exception as e:
            log.exception(e)

    def _create_post_like(self, user_id):
        try:
            likes = 0
            user = User.objects.get(id=user_id)
            while likes <= self.config.max_likes_per_user:
                post = next(self._generate_random_post(user))
                like_or_dislike = random.choice([True, False])
                if not post.likes.filter(
                        user=user, like=like_or_dislike).exists():
                    post.likes.create(user=user, like=like_or_dislike)
                    log.info(
                        "User %s %s post %s" % (user.email,
                                                ('liked' if like_or_dislike
                                                 else 'disliked'), post.post))
                    likes += 1
        except StopIteration:
            self.stop()

    def generate_random_emails(self):
        try:
            domains = [
                'tradecore.com',
                'twitter.com',
                'fb.com',
                'google.com',
                'linkedin.com',
                'github.com',
                'gitlab.com',
                'synerzip.com',
                'tradingtechnologies.com',
                'synechron.com',
                'clearbit.com',
            ]
            people = clearbit.Prospector.search(
                domain=random.choice(domains),
                email=True,
                page_size=self.config.number_of_users)
            self.new_user_emails = [
                person['email'] for person in people['results']
            ]
        except Exception as e:
            log.exception(e)

    def stop(self):
        sys.exit()


class AutoBot(BotConfig):
    def start(self):
        self.generate_random_emails()
        self.activity_signup()
        self.activity_post_create()
        self.activity_post_like()

    def activity_signup(self):
        with ThreadPoolExecutor() as executor:
            executor.map(self._perform_signup, self.new_user_emails)

    def activity_post_create(self):
        with ThreadPoolExecutor() as executor:
            executor.map(self._create_random_post, self.new_user_emails)

    def activity_post_like(self):
        post_users = Post.objects.annotate(total_likes=Count('likes')).filter(
            Q(
                Q(total_likes__lt=self.config.max_likes_per_user)
                | Q(total_likes__gt=0))).distinct().values('owner')
        with ThreadPoolExecutor() as executor:
            executor.map(self._create_post_like, post_users)

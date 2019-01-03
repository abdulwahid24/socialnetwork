from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel
from django_hstore import hstore

# Create your models here.


class Post(TimeStampedModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = hstore.DictionaryField()

    objects = hstore.HStoreManager()

    class Meta:
        db_table = 'user_post'
        verbose_name = "User Post"
        verbose_name_plural = "User Posts"

    def __str__(self):
        return "Post: %d" % self.id


class PostLike(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField()

    class Meta:
        db_table = 'user_post_like'
        verbose_name = "User Post Like"
        verbose_name_plural = "User Post Likes"
        unique_together = ("user", "post")

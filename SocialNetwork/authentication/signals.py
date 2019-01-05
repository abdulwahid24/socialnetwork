import json
import clearbit

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from authentication.models import User, Profile
from authentication.utility import extract_dict

clearbit.key = settings.CLEARBIT_API_KEY


@receiver(post_save, sender=User)
def fetch_profile(sender, *args, **kwargs):
    if kwargs.get('created'):
        user_instance = kwargs['instance']
        response = clearbit.Enrichment.find(
            email=user_instance.email, stream=True)
        response = extract_dict(response) if isinstance(response,
                                                        dict) else response
        profile = Profile(user=user_instance, data=response)
        profile.save()

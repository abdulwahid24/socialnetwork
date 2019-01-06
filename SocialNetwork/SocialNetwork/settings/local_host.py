from SocialNetwork.common_settings import *

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'socialNetworkDB',
        'HOST': '0.0.0.0',
        'PORT': '5433',
        'USER': 'postgres',
        'PASSWORD': 'SocialNetwork123#'
    }
}

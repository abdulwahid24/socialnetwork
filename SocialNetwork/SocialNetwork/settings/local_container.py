from SocialNetwork.common_settings import *

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'socialNetworkDB',
        'HOST': 'db',
        'PORT': '5432',
        'USER': 'postgres',
        'PASSWORD': 'SocialNetwork123#'
    }
}

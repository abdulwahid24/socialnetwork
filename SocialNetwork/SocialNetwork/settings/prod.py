from SocialNetwork.common_settings import *

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# NOTE:
# As of now prod is same as dev_lambda

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd3tid9uhbcniaj',
        'HOST': 'ec2-54-235-199-36.compute-1.amazonaws.com',
        'PORT': '5432',
        'USER': 'zydmxrzfbwdjpx',
        'PASSWORD': 'S4uqobgVUq2YNx528HbV9kqbiT'
    }
}

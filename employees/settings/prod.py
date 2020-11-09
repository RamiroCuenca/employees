from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd98erqhde1pu6v',
        'USER': 'buzvghbyxbifzm',
        'PASSWORD': 'ec480e7cde5bde960d2733b05cb9cc9ddf6c10accb739040a590ef5195f9c8b3',
        'HOST': 'ec2-54-159-107-189.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

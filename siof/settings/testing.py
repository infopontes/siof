import os

from .settings import *

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR / 'db_teste.sqlite3'),
    }
}
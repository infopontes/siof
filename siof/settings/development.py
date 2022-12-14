import os
from decouple import config, Csv

from .settings import *

DEBUG = True


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY_DEV')

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR / 'db_dev.sqlite3'),
    }
}
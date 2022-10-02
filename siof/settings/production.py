import os

from .settings import *

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# Adicionar o IP quando subir o ambiente de produção
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '<database_hostname_or_ip>',
        'PORT': '<database_port>',
    }
}
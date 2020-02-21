# coding: utf-8

import os, sys


try:
    LOCAL_HOST_ADDR = sys.argv[2]
except:
    LOCAL_HOST_ADDR = '127.0.0.1:8000'

URL = 'http://%s/' % LOCAL_HOST_ADDR

DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'OPTIONS':  {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

if 'test' in sys.argv or 'test_coverage' in sys.argv:
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
    DATABASES['default']['OPTIONS'] = {}


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_ROOT = '%sstatic/' % URL
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

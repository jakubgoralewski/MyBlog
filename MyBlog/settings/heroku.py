# -*- coding: utf-8 -*-
from .base import *
import dj_database_url

DEBUG = os.environ.get('DEBUG')
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG

SECRET_KEY = os.environ.get('DEBUG')

DATABASES = {
    'default': dj_database_url.config()
}

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

DATABASE_OPTIONS = {"use_unicode": True, "charset": 'utf8', 'autocommit': True, }

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(levelname)s %(asctime)s %(process)d%(module)s\t%(message)s'  # '%(levelname)s %(asctime)s %(module)s%(process)d %(thread)d %(message)s'
            },
        },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(PROJECT_PATH, 'django.log'),
            'formatter': 'standard',
            },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
            }
        },
    'loggers': {
        'django': {
            'handlers': ['console', 'default'],
            'level': 'DEBUG',
            'propagate': False,
            },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
            },
        }
    }
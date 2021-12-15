from .base import *
from .db import SQLITE

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = SQLITE

#Archivos
STATIC_URL = '/static/'
STATIC_ROOT  = os.path.join(BASE_DIR, 'staticfiles/')

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

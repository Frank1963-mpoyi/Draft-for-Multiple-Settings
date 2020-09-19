from .base                              import *

import dj_database_url

from .base                              import *


DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = []

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]


#DATABASES['default'] =  dj_database_url.config()

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
#BASE_PATH = os.path.join(BASE_DIR)
#APP_STATIC = 'weather/static/'       #location of static file 

STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_PATH, APP_STATIC)  #location of static file root collect static file
#
MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_PATH, f'{APP_STATIC}/media')


# NB:
# REview related to Horuku Whitenoise
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'


# NB:
#related to Horuku review
#import dj_database_url
#prod_db  =  dj_database_url.config(conn_max_age=500)
#DATABASES['default'].update(prod_db)

# OR 
 
 # Heroku: Update database configuration from $DATABASE_URL.
##import dj_database_url
#db_from_env = dj_database_url.config(conn_max_age=500)
#DATABASES['default'].update(db_from_env)



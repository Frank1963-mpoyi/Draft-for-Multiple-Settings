from .base                              import *
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


M_DIR = os.path.join(BASE_DIR, 'Draft/')

parser = configparser.ConfigParser()
parser.read_file(open(os.path.join(M_DIR, 'app.ini')))

DATABASES = {
    'default': {
       
        'ENGINE'    : 'django.db.backends.postgresql',
        'NAME'      : parser.get('draft_app', 'name'),
        'USER'      : parser.get('draft_app', 'user'),
        'PASSWORD'  : parser.get('draft_app', 'password'),
        'HOST'      : parser.get('draft_app', 'host') or '127.0.0.1',
        'PORT'      : parser.getint('draft_app', 'port') or '5432',

    }
}


#DATABASES = {'default': dj_database_url.config(default='postgres://postgres:paulin63@localhost:5432/draft')}
#DATABASES = {'default': dj_database_url.config(default='postgres://user:pass@localhost/dbname')}

#DATABASES = {
    #'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
#}


 #DEBUG TOOLBAR SETTINGS
DEBUG_TOOLBAR_PANELS = [
     'debug_toolbar.panels.versions.VersionsPanel',
     'debug_toolbar.panels.timer.TimerPanel',
     'debug_toolbar.panels.settings.SettingsPanel',
     'debug_toolbar.panels.headers.HeadersPanel',
     'debug_toolbar.panels.request.RequestPanel',
     'debug_toolbar.panels.sql.SQLPanel',
     'debug_toolbar.panels.staticfiles.StaticFilesPanel',
     'debug_toolbar.panels.templates.TemplatesPanel',
     'debug_toolbar.panels.cache.CachePanel',
     'debug_toolbar.panels.signals.SignalsPanel',
     'debug_toolbar.panels.logging.LoggingPanel',
     'debug_toolbar.panels.redirects.RedirectsPanel',
     'debug_toolbar.panels.profiling.ProfilingPanel',
     ]

def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS'   : False,
    'SHOW_TOOLBAR_CALLBACK' : show_toolbar,
    }

#ENVIRONMENT = 'DEVELOPMENT'

#print("\n")
#print("DEBUG        = ", DEBUG)
#print("MODE         = ", ENVIRONMENT)
#print("STATIC_ROOT  = ", STATIC_ROOT)
#print("MEDIA_ROOT   = ", MEDIA_ROOT)
#print("\n")

# In file app.ini
#[draft_app]

#name = postgres
# #user = postgres
#password = paulin63
# #host = localhost
#port = 5432
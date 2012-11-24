# Django settings for arbol project.

import os

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
os.environ['arbol_path'] = PROJECT_PATH

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
    ('german', 'ger.morab@gmail.com'),
    ('johanna', 'johanna.roa@gmail.com'),
)

#DEFAULT_FROM_EMAIL = 'proyarbolbosque@gmail.com'
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = 'proyarbolbosque@gmail.com'
#EMAIL_HOST_PASSWORD = 'frijoles_55'
#EMAIL_USE_TLS = True
#EMAIL_SUBJECT_PREFIX = "[ Arbol Bosque ]"

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'arbol',                      # Or path to database file if using sqlite3.
        'USER': 'arbol',                      # Not used with sqlite3.
        'PASSWORD': 'arbolpass',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Bogota'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/home/german/workspace/proyecto/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/bosque/static/'



# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'bosque','static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'dajaxice.finders.DajaxiceFinder',
)

DAJAXICE_MEDIA_PREFIX="dajaxice"
DAJAXICE_NOTIFY_EXCEPTIONS = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ip#b=h+q#w^^musz25#tg=wj_cqwse-bncqwel%ycj3m91xvh^'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
                               "django.core.context_processors.request",
                               "django.core.context_processors.debug",
                               "django.core.context_processors.i18n",
                               "django.core.context_processors.media",
                               "django.core.context_processors.static",
                               "django.contrib.messages.context_processors.messages",
                               #"django.contrib.messages.context_processors.request"
                               )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'arbol.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'arbol.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'bosque','templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'dajaxice',
    'dajax',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'arbol.bosque',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d: %(message)s'
        },
        'simple': {
#            'format': '%(levelname)s %(asctime)s %(pathname)s %(funcName)s %(process)d %(thread)d: %(message)s'
            'format': '%(levelname)s %(asctime)s: %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'general_file':{
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': PROJECT_PATH+'/logs/general.log',
                'formatter': 'simple'
        },
        'dajaxice_file':{
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': PROJECT_PATH+'/logs/dajaxice.log',
                'formatter': 'simple'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['general_file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'dajaxice': {
            'handlers': ['dajaxice_file'],
            'level': 'WARNING',
            'propagate': True,
        },
    }
}

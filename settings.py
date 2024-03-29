
DATABASES = {
	'default': {
		'ENGINE':	'django.db.backends.mysql',
		'NAME':		'django-mediacenter',
		'USER': 	'Django',
		'PASSWORD':	'',
		'HOST':		'',
		'PORT':		'',
		}
	}
DATABASES['django-mediacenter'] = DATABASES['default']

home = '/home/code/django-mediacenter/'
TEMPLATE_DIRS = (
		home,
		home+"Music/",
		home+"Movies/",
		home+"Radio/",
		home+"Player/",
		)


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('webmaster', 'webmaster@localhost'),
)

MANAGERS = ADMINS

SECRET_KEY = ''

TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'Django.urls'

INSTALLED_APPS = (
#    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)


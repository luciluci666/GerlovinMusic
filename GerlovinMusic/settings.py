"""
Django settings for GerlovinMusic project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import socket
from pathlib import Path
import os,sys
from unicodedata import name

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

PRJOJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PRJOJECT_ROOT, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w^!(6n%tojupti(lszo71i*ay0j0wtph*n1+30l&640+$40f#h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = [
    "127.0.0.1",
    "192.168.2.77"
]

SERVER_IP = socket.gethostbyname(socket.gethostname())

# Application definition

INSTALLED_APPS = [
    'music.apps.MusicConfig',
    'grappelli',
    'tinymce',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'GerlovinMusic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PRJOJECT_ROOT, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'GerlovinMusic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if SERVER_IP == '83.229.83.226':
    DATABASES = {
        ### sqllite ###
        # 'default': {
        #     'ENGINE': 'django.db.backends.sqlite3',
        #     'NAME': BASE_DIR / 'db.sqlite3',
        # }

        ### mysql local ###
        # 'default': {
        #     'NAME' : 'gerlovinmusic',
        #     'ENGINE': 'django.db.backends.mysql',
        #     'USER' : 'root',
        #     'PASSWORD' : 'papanhb2022',
        #     'HOST' : 'localhost',
        #     'PORT' : '7000',
        # },

        ### mysql server ###
        'default': {
            'NAME' : 'gerlovinmusic',
            'ENGINE': 'django.db.backends.mysql',
            'USER' : 'gerlovinmusic',
            'PASSWORD' : 'papanhb2022',
            'HOST' : 'localhost',
        }
    }
else:
    DATABASES = {
    ### sqllite ###
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }

    ### mysql local ###
    'default': {
        'NAME' : 'gerlovinmusic',
        'ENGINE': 'django.db.backends.mysql',
        'USER' : 'root',
        'PASSWORD' : 'papanhb2022',
        'HOST' : 'localhost',
        'PORT' : '7000',
    },
}



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PRJOJECT_ROOT, 'static')
STATICFILES_DIRS = (
    os.path.join(PRJOJECT_ROOT, 'static', 'static_files'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(STATICFILES_DIRS[0], 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.mail.ru'
EMAIL_PORT=25
EMAIL_HOST_USER='gerl.adm@mail.ru'
EMAIL_HOST_PASSWORD='MN97MUcPbssts7nNymbu'
EMAIL_USE_TLS=True




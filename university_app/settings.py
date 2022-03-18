"""
Django settings for university_app project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import django_heroku
import os 
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7cg*@rterr)h%uhye=pj@hkndvfiopad%7u8aypsd00pxzq7bf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOED_HOSTS = ['127.0.0.1','eagertolearn.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "rest_framework",
    "manage_accounts",  "corsheaders",
    # "profiles",
    "app_contents",
    'django.contrib.staticfiles',
]

#  "whitenoise.middleware.WhiteNoiseMiddleware"
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]


CORS_ALLOW_ALL_ORIGINS=True

# 'DEFAULT_PARSER_CLASSES': (
#     'rest_framework.parsers.JSONParser',
#     'rest_framework.parsers.FormParser',
#     'rest_framework.parsers.MultiPartParser',
# )

ROOT_URLCONF = 'university_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'university_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
# ! With MongoDb
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'name':"university_app",
        'CLIENT':{
            'host':"mongodb+srv://manas2342:ilyalexa@contact-book.z6uhs.mongodb.net/university_app?retryWrites=true&w=majority",
            'authMechanism': 'SCRAM-SHA-1'
        }
    }
}
# mongodb+srv://manas2342:<password>@contact-book.z6uhs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority

AUTH_USER_MODEL="manage_accounts.MyUser"


REST_FRAMEWORK = {
    
  

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
    
    
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


# serve file 
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    
]
# combininig to all static files into staticfiles folder
STATIC_ROOT=BASE_DIR /'static'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


MEDIA_ROOT=BASE_DIR / 'media'

MEDIA_URL='media/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Activate Django-Heroku.
django_heroku.settings(locals())
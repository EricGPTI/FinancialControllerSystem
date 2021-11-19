import os
from decouple import config
from decouple import Csv
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

COLLECTFAST_ENABLED = False

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# AWS S3
#AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
#
#if AWS_ACCESS_KEY_ID:
#    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
#    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
#    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age-86400', }
#    AWS_PRELOAD_METADATA = True
#    AWS_AUTO_CREATE_BUCKET = False
#    AWS_QUERYSTRING_AUTH = True
#    AWS_S3_CUSTOM_DOMAIN = None
#    COLLECTFAST_ENABLED = True
#
#    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
#    AWS_DEFAULT_ACL = 'None'
#
#    # Static Assets
#    # ----------------------------------------------------------------------------
#    STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
#    COLLECTFAST_STRATEGY = "collectfast.strategies.boto3.Boto3Strategy"
#    STATIC_S3_PATH = 'static/'
#    STATIC_ROOT = f'/{STATIC_S3_PATH}/'
#    STATIC_URL = f'//s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/{STATIC_S3_PATH}/'
#    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
#
#    # Upload Media Folder
#    # ----------------------------------------------------------------------------
#    DEFAULT_STORAGE = 's3_folder_storage.s3.DefaultStorage'
#    DEFAULT_S3_PATH = 'media'
#    MEDIA_ROOT = f'/{DEFAULT_S3_PATH}/'
#    MEDIA_URL = f'//s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/{DEFAULT_S3_PATH}/'
#
#    INSTALLED_APPS.append('s3_folder_storage')
#    INSTALLED_APPS.append('storages')
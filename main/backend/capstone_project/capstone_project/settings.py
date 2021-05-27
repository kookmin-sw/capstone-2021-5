"""
Django settings for capstone_project project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@#!tz#jj#(fr1*m=ow=d+_ujlhb8w3tg5$#zn0@aol)2f+ak6k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = [
#     ".ap-northeast-2.compute.amazonaws.com",
#     ".ksentio.com",
# ]

ALLOWED_HOSTS = ["*"]
# Application definition

INSTALLED_APPS = [
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account_app',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'django.contrib.sites',
    'rest_framework',
    'corsheaders',
    'allauth.socialaccount',
    'analysis',
     'chat',
     'diary_app',
]
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]
AUTH_USER_MODEL = 'account_app.customUser'
ROOT_URLCONF = 'capstone_project.urls'

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

WSGI_APPLICATION = 'capstone_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


import my_settings

DATABASES = my_settings.DATABASES


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False  

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        #  'rest_framework.permissions.AllowAny',      # 누구나 접근 가능

    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        #'rest_framework.authentication.SessionAuthentication',
        #'rest_framework.authentication.BasicAuthentication',
    ),
}

#ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_REQUIRED = False
# ACCOUNT_UNIQUE_EMAIL = True 
ACCOUNT_USERNAME_REQUIRED = True

#ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_VERIFICATION = "none"

REST_USE_JWT = True
ACCOUNT_LOGOUT_ON_GET = True

# CORS 관련 추가 
CORS_ORIGIN_ALLOW_ALL=True
CORS_ALLOW_CREDENTIALS = True

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'account_app.serializers.CustomRegisterSerializer',
}
ACCOUNT_ADAPTER = 'account_app.adapter.DefaultAccountAdapterCustom'

JWT_AUTH = {
'JWT_ENCODE_HANDLER':
'rest_framework_jwt.utils.jwt_encode_handler',

'JWT_DECODE_HANDLER':
'rest_framework_jwt.utils.jwt_decode_handler',

'JWT_PAYLOAD_HANDLER':
'rest_framework_jwt.utils.jwt_payload_handler',

'JWT_PAYLOAD_GET_USER_ID_HANDLER':
'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

'JWT_RESPONSE_PAYLOAD_HANDLER':
'rest_framework_jwt.utils.jwt_response_payload_handler',

'JWT_SECRET_KEY': SECRET_KEY,
'JWT_GET_USER_SECRET_KEY': None,
'JWT_PUBLIC_KEY': None,
'JWT_PRIVATE_KEY': None,
'JWT_ALGORITHM': 'HS256',
'JWT_VERIFY': True,
'JWT_VERIFY_EXPIRATION': True,
'JWT_LEEWAY': 0,
'JWT_EXPIRATION_DELTA': datetime.timedelta(days=10),
'JWT_AUDIENCE': None,
'JWT_ISSUER': None,

'JWT_ALLOW_REFRESH': False,
'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=30),

'JWT_AUTH_HEADER_PREFIX': 'JWT',
'JWT_AUTH_COOKIE': None,

}

# Channels
ASGI_APPLICATION = 'capstone_project.routing.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('https://www.ksentio.com:80', 6379)],
        },
    },
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
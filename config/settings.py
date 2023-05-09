"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%9g$@k$e(b^r^=-nwm2*9(oq*xkc_uu79b!2tihm3q!(m+c&c='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.contenttypes',

    'corsheaders',
    'baton',
    'colorfield',
    'extra_settings',
    'filebrowser',
    'tinymce',
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',
    'django_celery_results',
    'django_celery_beat',
    'debug_toolbar',
    'django_filters',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'events',
    
    'djoser',
    'baton.autodiscover',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'watson.middleware.SearchContextMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME":  BASE_DIR / "db.sqlite3",
        "USER": "user",
        "PASSWORD": "SQL_PASSWORD",
        "HOST": "localhost",
        "PORT": "5432",
    }
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

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [BASE_DIR / 'static']


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Media files

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'


# REST framework settings

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    ],
    'DEFAULT_METADATA_CLASS': 'rest_framework.metadata.SimpleMetadata',
    'DEFAULT_PAGINATION_CLASS': 'config.pagination.CustomPagination',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'PAGE_SIZE': 12
}


# JWT Authentication settings

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT', 'Bearer'),
}


# django-debug-toolbar settings

INTERNAL_IPS = ["127.0.0.1"]


# Django CORS headers setttings

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_CREDENTIALS = True


# Djoser settings

DJOSER = {
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': False,
    'SERIALIZERS': {
        'user': 'login.serializers.CustomUserSerializer',
        'current_user': 'login.serializers.CustomUserSerializer',
        'user_create': 'login.serializers.CustomUserCreateSerializer'
    }
}


# Django baton settings

BATON = {
    'SITE_HEADER': 'Администрирование',
    'SITE_TITLE': 'Администрирование мероприятий',
    'INDEX_TITLE': ' ',
    'COPYRIGHT': 'copyright © 2023 <a href="https://github.com/Re-Gelu">made by Re;Gelu</a>',  # noqa
    'POWERED_BY': '<a href="https://github.com/Re-Gelu">Re;Gelu</a>',
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
    'ENABLE_IMAGES_PREVIEW': True,
    'CHANGELIST_FILTERS_IN_MODAL': True,
    'CHANGELIST_FILTERS_ALWAYS_OPEN': False,
    'CHANGELIST_FILTERS_FORM': True,
    'MENU_ALWAYS_COLLAPSED': False,
    'MENU_TITLE': 'Меню',
    'MESSAGES_TOASTS': False,
    'GRAVATAR_DEFAULT_IMG': 'retro',
    'LOGIN_SPLASH': '/static/core/img/login-splash.png',
}


# Filebrowser settings

FILEBROWSER_DIRECTORY = ''

FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Миниатюра (1 кол.)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'small': {'verbose_name': 'Маленькая (2 кол.)', 'width': 140, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Средняя (4 кол.)', 'width': 300, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Большая (6 кол.)', 'width': 460, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Огромная (8 кол.)', 'width': 680, 'height': '', 'opts': ''},
}

# TinyMCE settings

TINYMCE_FILEBROWSER = True

TINYMCE_DEFAULT_CONFIG = {
    "theme": "silver",
    "height": 600,
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
        "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
        "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
        "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
        "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
        "a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 20,
}

# Redis settings

REDIS_URL = 'redis://localhost:6379/0'


# Cache settings

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': REDIS_URL,
    },
    'cache_table': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table',
    }
}

CACHING_TIME = 60 * 5


# 'Extra settings' settings

EXTRA_SETTINGS_ENFORCE_UPPERCASE_SETTINGS = True

EXTRA_SETTINGS_CACHE_NAME = 'cache_table'


# Payment settings

QIWI_PRIVATE_KEY = ""

QIWI_PAYMENTS_LIFETIME = 30

SUCCESS_PAYMENT_URL = "http://127.0.0.1:8000/"


# Celery settings

CELERY_APP = 'config'

CELERY_BROKER_URL = REDIS_URL

CELERY_TASK_TRACK_STARTED = True

CELERY_TASK_TIME_LIMIT = 30 * 60

RESULT_BACKEND = REDIS_URL

CACHE_BACKEND = 'django-cache'

BEAT_SCHEDULE = {}


# Tests cache fix

if 'test' in sys.argv: 
    
    EXTRA_SETTINGS_CACHE_NAME = 'default'

    CACHES = {'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}}

EXTRA_SETTINGS_SHOW_TYPE_LIST_FILTER = True

EXTRA_SETTINGS_SHOW_NAME_PREFIX_LIST_FILTER = True

EXTRA_SETTINGS_FILE_UPLOAD_TO = "media/files/"

EXTRA_SETTINGS_IMAGE_UPLOAD_TO = "media/files/"

EXTRA_SETTINGS_VERBOSE_NAME = "Настройки проекта"

EXTRA_SETTINGS_DEFAULTS = [
    {
        "name": "QIWI_PRIVATE_KEY",
        "type": "text",
        "value": "",
        "description": "Приватный QIWI ключ. Получить можно тут: https://qiwi.com/p2p-admin/api. ОБЯЗАТЕЛЬНО К ИЗМЕНЕНИЮ!",
    },
    {
        "name": "QIWI_PAYMENTS_LIFETIME",
        "type": "int",
        "value": "30",
        "description": "Срок жизни QIWI счета на оплату (в мин)",
    },
]


# Prod settings

if os.environ.get("DEBUG") == '0':
    
    DEBUG = int(os.environ.get("DEBUG"))
    
    ALLOWED_HOSTS = str(os.environ.get("DJANGO_ALLOWED_HOSTS")).split(" ")
    
    CSRF_TRUSTED_ORIGINS = str(os.environ.get("CSRF_TRUSTED_ORIGINS")).split(" ")
    
    INTERNAL_IPS = str(os.environ.get("INTERNAL_IPS")).split(" ")
    
    SECRET_KEY = os.environ.get("SECRET_KEY")
    
    REDIS_URL = os.environ.get("REDIS_URL")
    
    QIWI_PRIVATE_KEY = os.environ.get("QIWI_PRIVATE_KEY")
    
    DATABASES = {
        "default": {
            "ENGINE": os.environ.get("SQL_ENGINE"),
            "NAME": os.environ.get("SQL_DATABASE"),
            "USER": os.environ.get("SQL_USER"),
            "PASSWORD": os.environ.get("SQL_PASSWORD"),
            "HOST": os.environ.get("SQL_HOST"),
            "PORT": os.environ.get("SQL_PORT"),
        }
    }
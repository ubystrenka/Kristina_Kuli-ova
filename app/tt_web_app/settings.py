from pathlib import Path

from decouple import config
from django.core.management.utils import get_random_secret_key

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = config('ENV_SECRET_KEY', default=get_random_secret_key())

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "tt_web_app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "tt_web_app.wsgi.application"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('ENV_DB_POSTGRES_NAME'),
        'USER': config('ENV_DB_POSTGRES_USER'),
        'PASSWORD': config('ENV_DB_POSTGRES_PASSWORD'),
        'HOST': config('ENV_DB_POSTGRES_HOST'),
        'PORT': config('ENV_DB_POSTGRES_PORT', cast=int),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = 'static/'


# Настройки Celery
CELERY_BROKER_URL = config('ENV_CELERY_BROKER')
CELERY_RESULT_BACKEND = config('ENV_CELERY_BROKER')
CELERY_BACKEND = config('ENV_CELERY_BACKEND')
CELERY_COUNTDOWN = config('ENV_CELERY_COUNTDOWN', cast=int)
CELERY_MAX_RETRIES = config('ENV_CELERY_MAX_RETRIES', cast=int)

CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
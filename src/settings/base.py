import os

import dj_database_url
from decouple import Csv, config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config("DJANGO_SECRET_KEY", default="topsecrettopsecrettopsecret")

DEBUG = config("DJANGO_DEBUG", default=1, cast=bool)

ALLOWED_HOSTS = config(
    "DJANGO_ALLOWED_HOSTS", default="localhost,127.0.0.1,0.0.0.0", cast=Csv()
)

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "django_filters",
    "drf_yasg",
    "storages",
    "src.api.images.apps.ImagesConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "src.urls"

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

WSGI_APPLICATION = "src.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        **dj_database_url.config(),
        "ENGINE": "django.db.backends.postgresql",
    },
}

CSRF_COOKIE_SECURE = config("DJANGO_CSRF_COOKIE_SECURE", default=1, cast=bool)
SESSION_COOKIE_SECURE = config("DJANGO_SESSION_COOKIE_SECURE", default=1, cast=bool)


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "pl"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

USE_AWS_S3 = config("USE_AWS_S3", default=0, cast=bool)

if USE_AWS_S3:
    AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID", default="")
    AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY", default="")
    AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME", default="")
    AWS_DEFAULT_ACL = config("AWS_DEFAULT_ACL", default="public-read")
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
    # s3 static settings
    AWS_LOCATION = "static"
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/"
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

else:
    STATIC_URL = "/static/"
    STATIC_ROOT = os.path.join(BASE_DIR, "static")


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

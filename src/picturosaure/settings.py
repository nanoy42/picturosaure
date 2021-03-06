"""
Django settings for picturosaure project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

SECRET_KEY = ""

DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core",
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

ROOT_URLCONF = "picturosaure.urls"

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
                "picturosaure.processors.conf_processor",
            ],
        },
    },
]

WSGI_APPLICATION = "picturosaure.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
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

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = "/media/"
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_ROOT = BASE_DIR / "media"

PICTUROSAURE_USE_WATERMARK = True
PICTUROSAURE_WATERMARK_MARGIN = 20
PICTUROSAURE_WATERMARK_COLOR = (255, 2155, 255, 128)
PICTUROSAURE_WATERMARK_SIZE = 100
PICTUROSAURE_WATERMARK_TEXT = "© "
PICTUROSAURE_WATERMARK_POS = "bottom-right"
PICTUROSAURE_TITLE = "Picturosaure"
PICTUROSAURE_CONTACT = "example@example.org"
PICTUROSAURE_LICENSE = """
Where not stated otherwise, the photograph is distributed under the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank">CC BY-NC-SA 4.0</a> license (attribution to ).
"""
PICTUROSAURE_LICENSE_NAME = ""

try:
    from picturosaure.local_settings import *
except:
    if "test" not in sys.argv or "test_coverage" in sys.argv:
        raise Exception("No local_settings.py file found in picturosaure directory")

if "test" in sys.argv or "test_coverage" in sys.argv:
    DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}
    SECRET_KEY = "b-nmqgd^$uo-%h_%wrp(07r9(p8q-2)ak5o_hds=2sx-)7py2@"

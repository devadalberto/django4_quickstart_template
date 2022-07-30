import environ
import os
from .base import *

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=True)

if READ_DOT_ENV_FILE:
    env.read_env(os.path.join(BASE_DIR, ".envdb"))

DEBUG = os.environ.get("DEV_DEBUG")

SECRET_KEY = os.environ.get("DEV_SECRET_KEY")

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")


DATABASES = {
    "default": {
        "ENGINE": env("SQL_ENGINE"),
        "HOST": env("DEV_SQL_HOST"),
        "NAME": env("DEV_SQL_DBNAME"),
        "USER": env("DEV_SQL_USER"),
        "PASSWORD": env("DEV_SQL_PASSWORD"),
        "PORT": env("SQL_PORT"),
    }
}

EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)

INSTALLED_APPS += ["django_extensions"]

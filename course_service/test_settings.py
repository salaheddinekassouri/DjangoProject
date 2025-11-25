# yourproject/test_settings.py
from .settings import *   # import base settings
import os
import logging

# --- Ensure tests run in non-prod mode ---
DEBUG = False

# --- DATABASE: Use PostgreSQL for tests ---
# Django will create the test database automatically if permissions allow.
POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT", "5432")
POSTGRES_USER = os.environ.get("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "postgres")
POSTGRES_DB = os.environ.get("POSTGRES_DB", "coursedb")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": POSTGRES_DB,
        "USER": POSTGRES_USER,
        "PASSWORD": POSTGRES_PASSWORD,
        "HOST": POSTGRES_HOST,
        "PORT": POSTGRES_PORT,
        # Optional: explicit test DB name Django will use (otherwise Django prefixes "test_")
        "TEST": {
            "NAME": os.environ.get("POSTGRES_TEST_DB", f"test_{POSTGRES_DB}"),
        },
    }
}

# --- Make tests faster: use MD5 password hasher ---
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

# --- Optional: show SQL in test logs (helpful for debugging) ---
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "loggers": {
        "django.db.backends": {
            "handlers": ["console"],
            "level": os.environ.get("DJANGO_SQL_LOG_LEVEL", "DEBUG"),
        },
    },
}

# --- Keep static settings minimal for tests ---
STATIC_URL = "/static/"

# --- Use an in-memory cache for tests (optional speedup) ---
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

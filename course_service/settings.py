from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "changeme-in-prod")

DEBUG = os.environ.get("DEBUG", "True") == "True"

ALLOWED_HOSTS = ["*"]


# -----------------------------------
# INSTALLED APPS (Prometheus added)
# -----------------------------------

INSTALLED_APPS = [
    'django_prometheus',          # Prometheus monitoring
    'courses',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


# -----------------------------------
# MIDDLEWARE (Prometheus added)
# -----------------------------------

MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware',
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django_prometheus.middleware.PrometheusAfterMiddleware',
]


ROOT_URLCONF = 'course_service.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'course_service.wsgi.application'


# -----------------------------------
# DATABASE: PostgreSQL
# -----------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'coursedb_tfpi',     # from Render: Database
        'USER': 'coursedb_tfpi_user',             # from Render: Username
        'PASSWORD': 'DQ74OcBEtq0yXF91ZD1icwkyHGru8WOv',     # from Render: Password
        'HOST': 'dpg-d4j3t2idbo4c73bc9mq0-a',         # from Render: Hostname
        'PORT': '5432',                  # default Postgres port
    }
}



# -----------------------------------
# PASSWORD VALIDATION
# -----------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# -----------------------------------
# INTERNATIONALIZATION
# -----------------------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# -----------------------------------
# STATIC FILES
# -----------------------------------

STATIC_URL = 'static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

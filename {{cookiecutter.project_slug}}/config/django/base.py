import os

import django
from config.env import env, BASE_DIR
from django.utils.encoding import smart_str
from django.utils.translation import gettext

django.utils.encoding.smart_text = smart_str
django.utils.translation.ugettext = gettext

env.read_env(os.path.join(BASE_DIR, ".env"))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=g&ji-4pp*d$fv3^5f(c-1$#!la=1vs^yp=0fy*8$^(5$4jtmo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])

# Application definition
LOCAL_APPS = [
{%- if cookiecutter.use_simple_user_app == "y" %}
    'applications.user',
{%- endif %}
{%- if cookiecutter.use_jwt == "y" %}
    'applications.authentication',
{%- endif %}
]

THIRD_PARTY_APPS = [
    'rest_framework',
{%- if cookiecutter.use_jwt == "y" %}
    'rest_framework_simplejwt',
{%- endif %}
    'drf_spectacular',
    'django_prometheus',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]

MIDDLEWARE = [
    {%- if cookiecutter.use_metrics == "y" %}
    'django_prometheus.middleware.PrometheusBeforeMiddleware',
    {%- endif %}
    # should be at the first
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # should be at the end
    {%- if cookiecutter.use_metrics == "y" %}
    'django_prometheus.middleware.PrometheusAfterMiddleware',
    {%- endif %}
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
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

postgres = env.json("POSTGRES_DATABASE")
DATABASES = {
    'default': {
    {%- if cookiecutter.use_metrics == "y" %}
        'ENGINE': 'django_prometheus.db.backends.postgresql',
    {%- else %}
        'ENGINE': 'django.db.backends.postgresql',
    {%- endif %}
        'NAME': postgres.get("NAME"),
        'USER': postgres.get("USER"),
        'PASSWORD': postgres.get("PASSWORD"),
        'HOST': postgres.get("HOST"),
        'PORT': postgres.get("PORT", 5432),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

{%- if cookiecutter.use_simple_user_app == "y" %}
AUTH_USER_MODEL = "applications_user.User"
{%- endif %}


from config.settings.cors import *  # noqa
from config.settings.drf import *  # noqa
from config.settings.swagger import *  # noqa
{%- if cookiecutter.use_logging == "y" %}
from config.settings.logging import *  # noqa
{%- endif %}
{%- if cookiecutter.use_tracing == "y" %}
from config.settings.tracing import *  # noqa
{%- endif %}
{%- if cookiecutter.use_jwt == "y" %}
from config.settings.jwt import *  # noqa
{%- endif %}
# from config.settings.caches import *  # noqad

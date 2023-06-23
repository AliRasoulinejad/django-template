from config.env import env
from .base import *  # noqa

DEBUG = False

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

from config.settings.sentry import *  # noqa

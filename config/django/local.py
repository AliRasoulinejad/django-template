from .base import *  # noqa

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions'
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware"
]

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda _: True,
}

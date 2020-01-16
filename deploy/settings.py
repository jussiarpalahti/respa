
from respa.settings import *

# Get whitenoise for serving static files
try:
    place = MIDDLEWARE.index('django.middleware.security.SecurityMiddleware')
except ValueError:
    place = 0

MIDDLEWARE.insert(place, 'whitenoise.middleware.WhiteNoiseMiddleware')

import environ

deploy_env = environ.Env(
    USE_X_FORWARDED_HOST = (bool, False),
    SECURE_PROXY = (bool, False),
    MEDIA_ROOT = (str, "/usr/src/app/www")
)

USE_X_FORWARDED_HOST = deploy_env('USE_X_FORWARDED_HOST')

if deploy_env('SECURE_PROXY'):
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(module)s %(asctime)s %(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django.db': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'generic': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'requests': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': False,
        },
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        }
    }
}

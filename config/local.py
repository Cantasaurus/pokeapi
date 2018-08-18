from .settings import *  # NOQA

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pokeapi',
        'USER': 'danny_canter',
        'HOST': 'localhost',
        'PORT' : '5432',
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

DEBUG = True
TASTYPIE_FULL_DEBUG = True

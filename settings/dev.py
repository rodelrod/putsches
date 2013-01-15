from base import *
DEBUG=True
if 'test' in sys.argv:
    SOUTH_TESTS_MIGRATE=False
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}

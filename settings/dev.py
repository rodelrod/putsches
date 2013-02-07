from base import *
DEBUG=True
INSTALLED_APPS += (
        'django_extensions',
        'lettuce.django',
        )
if 'test' in sys.argv:
    SOUTH_TESTS_MIGRATE=False
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}
    TEMPLATE_STRING_IF_INVALID = 'INVALID EXPRESSION: %s'

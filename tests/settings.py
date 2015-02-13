SECRET_KEY = 'shhhhh'

INSTALLED_APPS = [
    'tests.mock',
    'silhouette',
    'django_nose',
]

SILHOUETTE_PATH = 'silhouette'

SILHOUETTE_THEME = 'theme'

TEST_RUNNER = 'django_nose.BasicNoseRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=silhouette',
    '--cover-inclusive',
    '--verbosity=1'
]

MIDDLEWARE_CLASSES = []

DATABASES = {}

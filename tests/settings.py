SECRET_KEY = 'shhhhh'

INSTALLED_APPS = [
    'tests.mock',
    'silhouette',
    'django_nose',
]


SILHOUETTE = {
    'THEME': 'test',
    'PATTERNS': {
        "form_test": (
            "{theme}/{form}.html",
        ),
        "field_test": (
            "{theme}/{form}-{field}-{widget}.html",
        ),
    }
}


TEST_RUNNER = 'django_nose.BasicNoseRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=silhouette',
    '--cover-inclusive',
    '--verbosity=2'
]

MIDDLEWARE_CLASSES = []

DATABASES = {}

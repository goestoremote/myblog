import blog.apps
from .base import *

DEBUG = True

# database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#override apps
INSTALLED_APPS += [
    'blog.apps.BlogConfig'

]
from .base import * 

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DEBUG = True

DATABASES = {
    'default': {
            'ENGINE': os.getenv('SQL_ENGINE', 'django.db.backends.sqlite3'),
            'NAME': 'django_api_test',
            'USER': os.getenv('SQL_USER', 'user'),
            'PASSWORD': os.getenv('SQL_PASSWORD', 'password'),
            'HOST': os.getenv('SQL_HOST', 'localhost'),
            'PORT': os.getenv('SQL_PORT', '5432'),
    },
    'tenant_db_1': {
            'ENGINE': os.getenv('SQL_ENGINE', 'django.db.backends.sqlite3'),
            'NAME': TENANTS_WITH_DB_NAME['amazon'],
            'USER': os.getenv('SQL_USER', 'user'),
            'PASSWORD': os.getenv('SQL_PASSWORD', 'password'),
            'HOST': os.getenv('SQL_HOST', 'localhost'),
            'PORT': os.getenv('SQL_PORT', '5432'),
    },
    'tenant_db_2': {
            'ENGINE': os.getenv('SQL_ENGINE', 'django.db.backends.sqlite3'),
            'NAME': TENANTS_WITH_DB_NAME['others'],
            'USER': os.getenv('SQL_USER', 'user'),
            'PASSWORD': os.getenv('SQL_PASSWORD', 'password'),
            'HOST': os.getenv('SQL_HOST', 'localhost'),
            'PORT': os.getenv('SQL_PORT', '5432'),
    }
}



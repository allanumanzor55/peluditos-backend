"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qy$36x7!9kid**_-n5-xe#xfv2^deh!wl-*hfhj8i2d$d)-e_&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'graphene_django',
    'backend_app',
    'backend_app.schema',
    'corsheaders',
    'pydantic',
    'graphene_gis',
    'django_filters'
]

GRAPHENE = {
    "SCHEMA": "backend_app.schema.scheme.scheme"
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware'
]

ROOT_URLCONF = 'config.urls'

CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
)
 
 # Permitir que los encabezados de solicitud de dominio cruzado, puede usar el valor predeterminado, el jefe de solicitud predeterminado es:
# from corsheaders.defaults import default_headers
# CORS_ALLOW_HEADERS = default_headers
 
CORS_ALLOW_HEADERS = (
    'accept',
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)
ALLOWED_HOSTS = ['*']
#CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

#CORS_ORIGIN_WHITELIST = ('http://localhost:8081','http://localhost:8082','http://localhost:8080')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'CLIENT': {
            'name': 'db_patitas',
            'host': 'mongodb+srv://admin:LuJnWkrpjwgIA3X6@patitas.pqw6o.mongodb.net/db_patitas?retryWrites=true&w=majority',
            'username': 'admin',
            'password':'LuJnWkrpjwgIA3X6',
            'authMechanism': 'SCRAM-SHA-1'
        }
    }
}

# import dj_database_url  
# db_from_env = dj_database_url.config(conn_max_age=500)  
# DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'


# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  
# STATIC_URL = '/static/'
# # Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (  
#     os.path.join(BASE_DIR, 'static'),
# )
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

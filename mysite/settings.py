"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os import environ
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = [os.path.join(BASE_DIR,'templates')]
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'diwt1z&xvhw$7d&6tv0li8e5ovu6$x0517kev$-c72_5dwb+70'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
        '*',
        ]


from os import environ
debug = not environ.get("APP_NAME","")
if not debug:
    import sae.const
    db_name = sae.const.MYSQL_DB
    name = sae.const.MYSQL_USER
    pwd = sae.const.MYSQL_PASS
    host = sae.const.MYSQL_HOST
    port = sae.const.MYSQL_PORT
    host_s = sae.const.MYSQL_HOST_S
    #host = 'w.rdc.sae.sina.com.cn'
    #port = '3307'
    #name = 'yx4kmjk3jk'
    #pwd = 'kz2xkmklkikyhz3hm2hlxi0iix0kz3j53y440013'
    #db_name = 'app_whynotwhy'
    #from sae._restful_mysql import monkey
    #monkey.patch()

else:
    db_name = "books"
    name = "yzr"
    pwd = "314159"
    host = "127.0.0.1"
    port = "3306"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': db_name,                      # Or path to database file if using sqlite3.
        'USER': name,                      # Not used with sqlite3.
        'PASSWORD': pwd,                  # Not used with sqlite3.
        'HOST': host,                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': port,                      # Set to empty string for default. Not used with sqlite3.
    }
}
# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'books',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

"""
Django settings for myshop project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-jbw&knkl3b9k=pe6j=1ti%-#q__b8iao4+zwextw9lzd^amv=q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [

    'account',
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # local app
    "shop",
    'cart',
    'orders',
     'payment',


    # third party apps
    'debug_toolbar',
]

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",    # django debug toolbar
]

ROOT_URLCONF = 'myshop.urls'

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
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CART_SESSION_ID = 'cart'

LOGIN_REDIRECT_URL = 'shop:product_list'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
]

# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_USE_TLS = True  
# EMAIL_HOST = 'smtp.gmail.com'  
# EMAIL_PORT = 587  
# EMAIL_HOST_USER = 'nabeel.arhamsoft@gmail.com'  
# EMAIL_HOST_PASSWORD = 'prince1018'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# CSRF_TRUSTED_ORIGINS = ['https://3196-202-166-170-106.ngrok-free.app']

# AUTH_USER_MODEL = 'account.CustomUser'
# Stripe settings
STRIPE_PUBLISHABLE_KEY = 'pk_test_51KnJm7InSFbjN8BpIidcpQfYbyUqv6JTFGFzINzz9oyMdFVFidXth1UqtlM4xP5rHLLdjluLRYlmGhLgDq8LqKFJ00dzRrwuFu' # Publishable key
STRIPE_SECRET_KEY = 'sk_test_51KnJm7InSFbjN8BpF2tmq2CiQ5YuL7LW6os9NtwXM8P5yiK0sE1xOy1p9oaM7l8pMCGSIDFhKSDJEJ5RmKShoZ2w004TLll2H1'
# Secret key
STRIPE_API_VERSION = '2022-08-01'



STRIPE_WEBHOOK_SECRET = 'whsec_023587eb50f520792be15c5dc906390ba4ff5595f471d7c5b5ac69303b0071ba'
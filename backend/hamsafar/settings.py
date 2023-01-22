from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-@&t%2@-d!-t$t3_!3(#x4dsmi9o@4&)7xrk+sa-^an2idq23s!'

DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "bootstrap_datepicker_plus",
    'django.contrib.gis',
    'django_extensions',
    'rest_framework',
    'jalali_date',
    'bootstrap5',
    'leaflet',
    'webpush',
    'azbankgateways',
    'main',
    'account',
    'dashboards',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hamsafar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'hamsafar.context_processors.is_passenger',
            ],
        },
    },
]

WSGI_APPLICATION = 'hamsafar.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'gis',
        'USER': 'mrjy',
        'PASSWORD': '123456789',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


WEBPUSH_SETTINGS = {
    "VAPID_PUBLIC_KEY": "BC1kblFI49fYq0SnzdAhKMbuepr_Dz2F3lCvJrjHFe6WEYasrgEcIkDgSe83mzS4qI7d7FrZ98VOBMR2PzJgj9Y",
    "VAPID_PRIVATE_KEY": "qnI9D_ookqaTEJQ-U0lQEZ7WL9baktZOxif4lsrdZ_Y",
    "VAPID_ADMIN_EMAIL": "goodbye001281@gmail.com"
}

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# LANGUAGE_CODE = 'fa-ir'
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'account.Users'

JALALI_DATE_DEFAULTS = {
    'Strftime': {
        'date': '%y/%m/%d',
        'datetime': '%H:%M:%S _ %y/%m/%d',
    },
    'Static': {
        'js': [
            # loading datepicker
            'admin/js/django_jalali.min.js',
            # OR
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.core.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/calendar.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc-fa.js',
            # 'admin/js/main.js',
        ],
        'css': {
            'all': [
                'admin/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css',
            ]
        }
    },
}

LEAFLET_CONFIG = {
    #     # conf here
    #     # 'SPATIAL_EXTENT': (5.0, 44.0, 7.5, 46)
    'DEFAULT_CENTER': [35.636940, 51.387863],
    #     'DEFAULT_ZOOM': 5,
    'MIN_ZOOM': 10,
    #     'MAX_ZOOM': 18,
    #     'DEFAULT_PRECISION': 6,

    'RESET_VIEW': False,
    'ATTRIBUTION_PREFIX': '',
}

AZ_IRANIAN_BANK_GATEWAYS = {
    'GATEWAYS': {
        # 'BMI': {
        #     'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
        #     'TERMINAL_CODE': '<YOUR TERMINAL CODE>',
        #     'SECRET_KEY': '<YOUR SECRET CODE>',
        # },
        # 'SEP': {
        #     'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
        #     'TERMINAL_CODE': '<YOUR TERMINAL CODE>',
        # },
        'ZARINPAL': {
            'MERCHANT_CODE': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
            'SANDBOX': 1,  # 0 disable, 1 active
        },
        # 'IDPAY': {
        #     'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
        #     'METHOD': 'POST',  # GET or POST
        #     'X_SANDBOX': 0,  # 0 disable, 1 active
        # },
        # 'ZIBAL': {
        #     'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
        # },
        # 'BAHAMTA': {
        #     'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
        # },
        # 'MELLAT': {
        #     'TERMINAL_CODE': '<YOUR TERMINAL CODE>',
        #     'USERNAME': '<YOUR USERNAME>',
        #     'PASSWORD': '<YOUR PASSWORD>',
        # },
        # 'PAYV1': {
        #     'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
        #     'X_SANDBOX': 0,  # 0 disable, 1 active
        # },
    },
    'IS_SAMPLE_FORM_ENABLE': True,  # اختیاری و پیش فرض غیر فعال است
    'DEFAULT': 'BMI',
    'CURRENCY': 'IRR',  # اختیاری
    'TRACKING_CODE_QUERY_PARAM': 'tc',  # اختیاری
    'TRACKING_CODE_LENGTH': 16,  # اختیاری
    'SETTING_VALUE_READER_CLASS': 'azbankgateways.readers.DefaultReader',  # اختیاری
    'BANK_PRIORITIES': [
        'ZARINPAL',
        # 'BMI',
        # 'SEP',
        # and so on ...
    ],  # اختیاری
}

from .base import *
import dj_database_url
# import django_heroku

ALLOWED_HOSTS = ['mga.herokuapp.com', '127.0.0.1']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

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

# STRIPE_PUBLIC_KEY = dc_config('STRIPE_PUBLIC_KEY')
# STRIPE_SECRET_KEY = dc_config('STRIPE_SECRET_KEY')

# db_from_env = dj_database_url.config()
# DATABASES['default'].update(db_from_env)
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}
# DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# django_heroku.settings(locals())

import os

from .development import *

DEBUG = True

ALLOWED_HOSTS = ['*', '127.0.0.1']

# os.environ.setdefault('DATABASE_HOST', '127.0.0.1')
# os.environ.setdefault('DATABASE_HOST', 'mysql')
os.environ.setdefault('DATABASE_HOST', '127.0.0.1')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{{project_name}}',
        'USER': 'root',
        # 'PASSWORD': 'sdRTYfv45@#',
        'PASSWORD': '123456789',
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}

#  # Security
# SESSION_COOKIE_SECURE = True
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_SECONDS = 31536000
# SECURE_REDIRECT_EXEMPT = []
# SECURE_SSL_HOST = None
# SECURE_SSL_REDIRECT = True
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

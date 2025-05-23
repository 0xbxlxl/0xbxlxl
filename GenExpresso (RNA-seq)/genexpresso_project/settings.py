"""
Django settings for genexpresso_project.

Generated by 'django-admin startproject' using Django 5.1.4.
"""

from pathlib import Path
import os

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*7l_9s1s9n4)in$3!cg(&c+&-fb)0vh@(&(j*%ksu%)0cf5ya3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Change to False in production

ALLOWED_HOSTS = []  # Add your production domain/IP when deploying

# Application definition
INSTALLED_APPS = [
    # My apps
    'genexpresso',
    'accounts',

    # Third-party apps
    'django_bootstrap5',
    
    # Default Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',  
    'django_auto_logout.middleware.auto_logout',
    'django.contrib.messages.middleware.MessageMiddleware',  # Ensure it's present before auto-logout
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'genexpresso_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Ensure templates are found
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

WSGI_APPLICATION = 'genexpresso_project.wsgi.application'

# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password Validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static Files Settings
STATIC_URL = '/static/'

# Ensure Django finds static files in development
STATICFILES_DIRS = [
    BASE_DIR / 'genexpresso/static',
]

# In production, collect static files here
STATIC_ROOT = BASE_DIR / 'staticfiles'

# CSP (Content Security Policy) Settings - Prevents JS blocking errors
CSP_DEFAULT_SRC = ("'self'",)  # Allow scripts from our own domain
CSP_SCRIPT_SRC = ("'self'",)  # Prevents eval() while allowing our JavaScript files
CSP_IMG_SRC = ("'self'", "data:")  # Allow images & icons
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")  # Allow inline styles if needed

# User Authentication & Session Management
LOGIN_REDIRECT_URL = 'genexpresso:index'
LOGOUT_REDIRECT_URL = 'genexpresso:logout_page'
LOGIN_URL = 'accounts:login'

# Auto logout settings
AUTO_LOGOUT = {
    'IDLE_TIME': 10,  # Logout after 10 minutes of inactivity
    'MESSAGE': 'The session has expired. Please login again to continue.'
}

# Session Settings
SESSION_COOKIE_AGE = 600  # 10 minutes before session expires
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Logout when browser closes
SESSION_SAVE_EVERY_REQUEST = True  # Update session on every request

# Collect Static Files in Development
if DEBUG:
    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)


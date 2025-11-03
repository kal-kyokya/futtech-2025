#!/usr/bin/env python3
"""
'settings/prod' modifies the base settings.py file to match a production environment.
"""

from .base import *

DEBUG = False

ALLOWED_HOSTS = env.list('DJANGO-ALLOWED_HOSTS', default=['kalkyokya.tech'])

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS', default=[])

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

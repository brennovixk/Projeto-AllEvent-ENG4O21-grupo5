"""
Django settings for AllEvent project.
"""
from pathlib import Path
import os

# BASE_DIR aponta para a pasta 'Projeto'
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "django-insecure-sp063i^kdyy^)-$l=0ar2w#()h#^&$-*u3bl_*$4q)@vx-g2w$"
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:8000', 'http://localhost:8000']

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'AllEvent', # App do projeto principal
    'core.apps.CoreConfig', # O novo app do seu time
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "AllEvent.urls"

# CORRIGIDO: Esta é a definição CORRETA E ÚNICA de TEMPLATES.
# 'APP_DIRS': True diz ao Django para procurar pastas 'templates'
# dentro de cada app (ou seja, ele vai achar 'core/templates' sozinho).
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [], # Não precisamos de DIRS globais, já que os templates estão no app 'core'
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

WSGI_APPLICATION = "AllEvent.wsgi.application"

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# CORRIGIDO: Caminho para os arquivos estáticos (CSS/JS)
# Ele vai procurar por uma pasta 'static' dentro de cada app (ex: 'core/static')
STATIC_URL = "static/"

# CORRIGIDO: Caminho para os arquivos de mídia (Imagens de eventos)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # Aponta para 'Projeto/media/'

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Configurações de Login/Logout
LOGIN_URL = '/accounts/login/' # Página de login do Django
LOGIN_REDIRECT_URL = '/' # Para onde vai depois do login
LOGOUT_REDIRECT_URL = '/' # Para onde vai depois do logout
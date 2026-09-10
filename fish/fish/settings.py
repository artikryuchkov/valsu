import os
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent
ON_RENDER = os.environ.get("RENDER") == "true"
DEBUG = not ON_RENDER and os.environ.get("DJANGO_DEBUG", "true").lower() == "true"
SECRET_KEY = os.environ.get("SECRET_KEY", "")
if not SECRET_KEY:
    if not DEBUG:
        raise ImproperlyConfigured("Set SECRET_KEY in environment variables")
    SECRET_KEY = "local-demo-only-never-use-in-production"
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
ALLOWED_HOSTS += [h.strip() for h in os.environ.get("ALLOWED_HOSTS", "").split(",") if h.strip()]
if os.environ.get("RENDER_EXTERNAL_HOSTNAME"):
    ALLOWED_HOSTS.append(os.environ["RENDER_EXTERNAL_HOSTNAME"])
INSTALLED_APPS = ["django.contrib.staticfiles", "form"]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
ROOT_URLCONF = "fish.urls"
TEMPLATES = [{"BACKEND": "django.template.backends.django.DjangoTemplates", "DIRS": [], "APP_DIRS": True, "OPTIONS": {"context_processors": []}}]
WSGI_APPLICATION = "fish.wsgi.application"
DATABASES = {}  # The demo needs no database or migrations.
LANGUAGE_CODE = "ru"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "public"]
# Only publish the new assets, never legacy form/static files.
STATICFILES_FINDERS = ["django.contrib.staticfiles.finders.FileSystemFinder"]
STORAGES = {"default": {"BACKEND": "django.core.files.storage.FileSystemStorage"}, "staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"}}
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https") if ON_RENDER else None
SECURE_SSL_REDIRECT = ON_RENDER
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SECURE_HSTS_SECONDS = 31536000 if ON_RENDER else 0
X_FRAME_OPTIONS = "DENY"

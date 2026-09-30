"""
Minimal Django settings for the Members admin import/export project.

This is a from-scratch scaffold: SQLite for zero-config local dev,
django-import-export wired into INSTALLED_APPS, and explicit
IMPORT_FORMATS / EXPORT_FORMATS so only the formats you asked for
(JSON, CSV, XLSX, HTML) show up as buttons in the admin.
"""

from pathlib import Path

from import_export.formats.base_formats import CSV, JSON, XLSX, HTML

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: replace this before deploying anywhere real.
SECRET_KEY = "django-insecure-replace-me-before-deploying"

DEBUG = True

ALLOWED_HOSTS: list[str] = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "import_export",
    "members",
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

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --- django-import-export -------------------------------------------------
# Only these formats are offered in the admin's Import / Export dialogs.
# HTML is export-only: there is no dependable round-trip HTML import format,
# so it's left out of IMPORT_FORMATS on purpose.
IMPORT_FORMATS = [CSV, JSON, XLSX]
EXPORT_FORMATS = [CSV, JSON, XLSX, HTML]

# Wrap each import in a DB transaction so a bad row rolls back the batch
# instead of leaving a partial import behind.
IMPORT_EXPORT_USE_TRANSACTIONS = True

# Skipped/skipped-with-errors rows are still reported in the import preview.
IMPORT_EXPORT_SKIP_ADMIN_LOG = False

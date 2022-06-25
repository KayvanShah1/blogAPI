import os
from dotenv import load_dotenv

load_dotenv()


def getenv_boolean(var_name, default_value=False):
    result = default_value
    env_value = os.getenv(var_name)
    if env_value is not None:
        result = env_value.upper() in ("TRUE", "1")
    return result


# Server Settings
SERVER_NAME = os.getenv("SERVER_NAME")
SERVER_HOST = os.getenv("SERVER_HOST")

# Project Settings
APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(APP_DIR)

SECRET_KEY = os.getenvb(b"SECRET_KEY")
if not SECRET_KEY:
    SECRET_KEY = os.urandom(32)

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8
BACKEND_CORS_ORIGINS = os.getenv("BACKEND_CORS_ORIGINS")

PROJECT_NAME = os.getenv("PROJECT_NAME", "FastAPI Project")
API_V1_PREFIX = "/api/v1"

# Database Settings
MONGODB_URI = os.getenv("MONGODB_URI")

# Templates Directory
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# Static files like CSS & Media files
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# E-Mailing Settings
SMTP_TLS = getenv_boolean("SMTP_TLS", True)
SMTP_SSL = getenv_boolean("SMTP_SSL", False)
SMTP_PORT = None
_SMTP_PORT = os.getenv("SMTP_PORT")
if _SMTP_PORT is not None:
    SMTP_PORT = int(_SMTP_PORT)
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

EMAILS_FROM_EMAIL = os.getenv("EMAILS_FROM_EMAIL")
EMAILS_FROM_NAME = PROJECT_NAME
EMAIL_RESET_TOKEN_EXPIRE_HOURS = 48
EMAIL_TEMPLATES_DIR = os.path.join(TEMPLATES_DIR, "email")
EMAILS_ENABLED = SMTP_HOST and SMTP_PORT and EMAILS_FROM_EMAIL

EMAIL_TEST_USER = "test@example.com"

USERS_OPEN_REGISTRATION = getenv_boolean("USERS_OPEN_REGISTRATION")

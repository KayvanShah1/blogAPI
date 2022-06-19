import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.getenvb(b"SECRET_KEY")
if not SECRET_KEY:
    SECRET_KEY = os.urandom(32)

PROJECT_NAME = os.getenv("PROJECT_NAME", "FastAPI Project")
API_V1_PREFIX = "/api/v1"

# Templates Directory
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# Static files like CSS & Media files
STATIC_ROOT = os.path.join(BASE_DIR, "static")

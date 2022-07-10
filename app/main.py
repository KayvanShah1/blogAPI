from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api import templates
from app.api.v1.api import api_router as api_v1_router
from app.core import settings


app = FastAPI(title=settings.PROJECT_NAME)

# Handle CORS protection
origins = settings.BACKEND_CORS_ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# register all the APIRouter Endpoints
app.include_router(templates.router)
app.include_router(api_v1_router, prefix=settings.API_V1_PREFIX)

# Static Files and Templates
app.mount("/static", StaticFiles(directory=settings.STATIC_ROOT), name="static")

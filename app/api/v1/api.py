from fastapi import APIRouter

from app.api.v1.endpoints import users, login

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(login.router, tags=["Authentication"])

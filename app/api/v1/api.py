from fastapi import APIRouter

from app.api.v1.endpoints import users, login, blog

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(blog.router, prefix="/blogs", tags=["Blogs"])
api_router.include_router(login.router, tags=["Authentication"])

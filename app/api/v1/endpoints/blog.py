from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder

from app.api.utils.security import get_current_user
from app.crud.blog import insert_blog
from app.schemas import custom_encoder
from app.schemas.blogs import BlogCreate, BlogResponse


router = APIRouter()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=BlogResponse,
    response_description="Successfully created a new blog",
)
async def create_blog(blog_content: BlogCreate, current_user=Depends(get_current_user)):
    blog_content = jsonable_encoder(blog_content, custom_encoder=custom_encoder)
    blog_content["author_name"] = current_user["full_name"]
    blog_content["author_id"] = current_user["_id"]

    created_blog_post = await insert_blog(blog_content)
    if not created_blog_post:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )
    return created_blog_post

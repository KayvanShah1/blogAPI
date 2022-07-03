from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
import pymongo

from app.api.utils.security import get_current_user
from app.crud.blog import insert_blog, find_blogs, find_blog, update_blog
from app.schemas import custom_encoder
from app.schemas.blogs import BlogCreate, BlogResponse, BlogUpdate
from app.schemas.msg import Message


router = APIRouter()


@router.post(
    "/create",
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


@router.get(
    "/",
    status_code=status.HTTP_302_FOUND,
    response_model=List[BlogResponse],
    response_description="Get all blog posts",
)
async def get_blog_posts(limit: int = 5, orderby: str = "created_at"):
    blogs = await find_blogs(sort_by={orderby: pymongo.DESCENDING}, limit=limit)
    return blogs


@router.get(
    "/{id}",
    status_code=status.HTTP_302_FOUND,
    response_model=BlogResponse,
    response_description="Get a blog post",
)
async def get_blog(id: str):
    blog = await find_blog(id)
    if blog is None:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT, detail=f"Blog Post {id} not found"
        )
    return blog


@router.put(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=BlogResponse,
    response_description="Updated a blog post",
)
async def update_blog_post(
    id: str, blog_content: BlogUpdate, current_user=Depends(get_current_user)
):
    if blog_post := await find_blog(id):
        if blog_post["author_id"] == current_user.get("_id"):
            updated_blog = await update_blog(
                id, jsonable_encoder(blog_content, custom_encoder=custom_encoder)
            )
            return updated_blog
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You are not the owner. Cannot modify/update the blog post. Access Denied",
            )

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Blog Post not found",
    )

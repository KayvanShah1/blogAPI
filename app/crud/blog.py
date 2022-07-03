from fastapi import HTTPException, status
from app.db.database import blogs_collection
from app.crud.utils import remove_none_from_data_dict


async def find_blog(id):
    return await blogs_collection.find_one({"_id": id})


async def find_blogs(sort_by: dict, limit: int):
    blogs = await blogs_collection.find().sort(sort_by.items()).to_list(length=limit)
    return blogs


async def insert_blog(blog_content: dict):
    new_blog_content = await blogs_collection.insert_one(blog_content)
    created_blog_post = await blogs_collection.find_one(
        {"_id": new_blog_content.inserted_id}
    )
    return created_blog_post


async def update_blog(id, blog_content: dict):
    blog_content = remove_none_from_data_dict(blog_content)
    if len(blog_content) >= 1:
        update_result = await blogs_collection.update_one(
            {"_id": id}, {"$set": blog_content}
        )
        if update_result.modified_count == 1:
            updated_blog_post = await find_blog(id)
            if updated_blog_post is not None:
                return updated_blog_post

    existing_blog_post = await find_blog(id)
    if existing_blog_post is not None:
        return existing_blog_post

    raise HTTPException(
        status_code=status.HTTP_304_NOT_MODIFIED,
        detail="Blog post not modified. Operation failed",
    )

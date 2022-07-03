from app.db.database import blogs_collection


async def insert_blog(blog_content: dict):
    new_blog_content = await blogs_collection.insert_one(blog_content)
    created_blog_post = await blogs_collection.find_one(
        {"_id": new_blog_content.inserted_id}
    )
    return created_blog_post

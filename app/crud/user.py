from app.db.database import users_collection


async def get_users(limit: int):
    blogs = await users_collection.find().to_list(length=limit)
    return blogs


async def add_user(user_data: dict):
    new_user = await users_collection.insert_one(user_data)
    created_user = await users_collection.find_one({"_id": new_user.inserted_id})
    return created_user

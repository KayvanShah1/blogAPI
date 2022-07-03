from app.db.database import users_collection


async def get_users():
    users = []
    users_list = users_collection.find()
    async for user in users_list:
        users.append(user)
    return users

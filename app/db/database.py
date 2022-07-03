from motor.motor_asyncio import AsyncIOMotorClient
from app.core.settings import MONGODB_URI


client = AsyncIOMotorClient(MONGODB_URI)
db = client.blogapi

users_collection = db["users"]
blogs_collection = db["blogs"]

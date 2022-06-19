import os

from motor.motor_asyncio import AsyncIOMotorClient


client = AsyncIOMotorClient(os.getenv("MONGODB_URL"))
db = client.blogapi

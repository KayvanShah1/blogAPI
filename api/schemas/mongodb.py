import os

import motor.motor_asyncio
from bson import ObjectId
from dotenv import load_dotenv

load_dotenv()


client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGODB_URL"))

# BSON and JSON compatibility addressed here
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

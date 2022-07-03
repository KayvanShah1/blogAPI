from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

from app.db.utils import PyObjectId


class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    full_name: Optional[str] = None
    created_at: datetime = datetime.utcnow()

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "username": "john_doe",
                "full_name": "John R. Doe",
                "email": "jdoe@example.com",
                "password": "secret_code",
            }
        }


class UserResponse(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str = Field(...)
    full_name: str = Field(...)
    email: EmailStr = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "username": "john_doe",
                "full_name": "John R. Doe",
                "email": "jdoe@example.com",
            }
        }


class UserDetails(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    updated_at: Optional[datetime]
    created_at: datetime


class UserUpdate(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: Optional[str] = Field(...)
    full_name: Optional[str] = Field(...)
    email: Optional[EmailStr] = Field(...)
    updated_at: datetime = datetime.utcnow()

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {"example": {"full_name": "John R. Doe", "password": "********"}}

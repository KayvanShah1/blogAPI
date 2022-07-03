from datetime import datetime
from bson import ObjectId

from pydantic import BaseModel, Field

from app.db.utils import PyObjectId


class BlogBase(BaseModel):
    title: str = Field(...)
    body: str = Field(...)


class BlogCreate(BlogBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    created_at: datetime = datetime.utcnow()

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "title": "Blog title",
                "body": "Blog content",
            }
        }


class BlogUpdate(BlogCreate):
    updated_at: datetime = datetime.utcnow()


class BlogResponse(BlogCreate):
    author_name: str = Field(...)
    author_id: str = Field(...)
    created_at: datetime | None
    updated_at: datetime | None

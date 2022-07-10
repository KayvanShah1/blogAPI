from datetime import datetime
from typing import Optional
from bson import ObjectId

from pydantic import BaseModel, Field

from app.db.utils import PyObjectId


class BlogBase(BaseModel):
    title: str = Field(...)
    body: str = Field(...)


class BlogCreate(BlogBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    created_at: Optional[datetime] = datetime.utcnow()

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "title": "Blog title",
                "body": "Blog content",
            }
        }


class BlogUpdate(BlogBase):
    updated_at: Optional[datetime] = datetime.utcnow()


class BlogResponse(BlogCreate):
    author_name: str
    author_id: str
    created_at: datetime
    updated_at: datetime | None

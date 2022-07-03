from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from app.db.utils import PyObjectId
from app.schemas import custom_encoder


class BlogBase(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    body: str = Field(...)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = custom_encoder
        schema_extra = {"example": {"title": "blog title", "body": "blog content"}}


class BlogContent(BlogBase):
    author_name: str = Field(...)
    author_id: str = Field(...)
    created_at: datetime = datetime.utcnow()
    updated_at: Optional[datetime]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = custom_encoder
        schema_extra = {
            "example": {
                "title": "Blog title",
                "body": "Blog content",
                "author_name": "Name of the author",
                "author_id": "ID of the author",
                "created_at": "Date of blog creation",
            }
        }


class BlogUpdate(BlogContent):
    updated_at: datetime = datetime.utcnow()


class BlogResponse(BlogContent):
    created_at: Optional[datetime] = Field(...)
    updated_at: Optional[datetime] = Field(...)

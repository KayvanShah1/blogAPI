from bson import ObjectId
from pydantic import BaseModel, Field

from mongodb import PyObjectId


class BlogContent(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    body: str = Field(...)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {"example": {"title": "blog title", "body": "blog content"}}


class BlogContentResponse(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    body: str = Field(...)
    author_name: str = Field(...)
    author_id: str = Field(...)
    created_at: str = Field(...)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "title": "Blog title",
                "body": "Blog content",
                "author_name": "Name of the author",
                "author_id": "ID of the author",
                "created_at": "Date of blog creation",
            }
        }

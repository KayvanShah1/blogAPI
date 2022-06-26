from pydantic import BaseModel, EmailStr, Field


class PasswordResetRequest(BaseModel):
    email: EmailStr = Field(...)


class PasswordReset(BaseModel):
    password: str = Field(...)

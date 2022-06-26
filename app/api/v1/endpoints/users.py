import secrets

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder

from app.api.utils.security import get_current_user
from app.core.security import get_password_hash
from app.db.database import db
from app.schemas.users import User, UserResponse, UserDetails
from app.utils.emails import send_registration_email

router = APIRouter()


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    response_description="Successfully registered a new user",
)
async def register_user(user_info: User):
    user_info = jsonable_encoder(user_info)

    # Find if the username already exists
    username_found = await db["users"].find_one({"name": user_info["name"]})
    if username_found:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Username already exists"
        )

    # Find if the email already exists
    email_found = await db["users"].find_one({"email": user_info["email"]})
    if email_found:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Email already exists"
        )

    # Hash the user password
    user_info["password"] = get_password_hash(user_info["password"])

    # Create an API Key for User
    user_info["api_key"] = secrets.token_hex(20)

    new_user = await db["users"].insert_one(user_info)
    created_user = await db["users"].find_one({"_id": new_user.inserted_id})

    # Send a registration email
    await send_registration_email(
        "Registration successful",
        user_info["email"],
        {"title": "Registration successful", "name": user_info["name"]},
    )

    return created_user


@router.post(
    "/details", response_description="Get User details", response_model=UserDetails
)
async def details(current_user=Depends(get_current_user)):
    user = await db["users"].find_one({"_id": current_user["_id"]})
    return user

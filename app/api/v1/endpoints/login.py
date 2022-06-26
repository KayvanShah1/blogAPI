from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.api.utils.security import get_current_user
from app.core.jwt import (
    create_access_token,
    access_token_jwt_subject,
    password_reset_request_subject,
    verify_access_token,
)
from app.core.security import get_password_hash, verify_password
from app.core import settings
from app.db.database import db
from app.schemas.msg import Message
from app.schemas.password import PasswordResetRequest, PasswordReset
from app.schemas.token import Token
from app.schemas.users import User, UserResponse
from app.utils.emails import send_password_reset_email


router = APIRouter()


@router.post(
    "/login/access-token",
    response_model=Token,
    status_code=status.HTTP_200_OK,
    response_description="Successfully logged In",
)
async def login(user_credentials: OAuth2PasswordRequestForm = Depends()):
    user = await db["users"].find_one({"name": user_credentials.username})
    if user and verify_password(user_credentials.password, user["password"]):
        access_token = create_access_token(
            payload={"id": user["_id"], "sub": access_token_jwt_subject}
        )
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid user credentials"
        )


@router.post("/login/test-token", response_model=UserResponse)
def test_token(current_user: User = Depends(get_current_user)):
    """
    Test access token.
    """
    return current_user


@router.post(
    "/password/reset-request",
    response_model=Message,
    response_description="Succesfully created a Password reset request",
)
async def password_reset_request(user_email: PasswordResetRequest):
    user = await db["users"].find_one({"email": user_email.email})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The user with this email does not exist in the system. Invalid E-mail address",
        )
    pwd_reset_token = create_access_token(
        payload={"id": user["_id"], "sub": password_reset_request_subject}
    )
    pwd_reset_link = f"{settings.SERVER_HOST}/password/reset?token={pwd_reset_token}"

    await send_password_reset_email(
        subject="Password Reset Instructions",
        email_to=user_email.email,
        body={
            "title": f"Password Reset Link for [{user['name']}]",
            "name": user["name"],
            "reset_link": pwd_reset_link,
            "password_reset_token": pwd_reset_token,
        },
    )
    return {"msg": "An E-mail has been sent with instructions to reset your password."}


@router.put(
    "/password/reset/", response_model=Message, response_description="Password Reset"
)
async def reset_password(token: str, new_password: PasswordReset):
    info = verify_access_token(token)
    if not info:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token"
        )

    user = await get_current_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found"
        )

    # Check if the new password is not NULL or NONE
    if new_password.password is None:
        raise TypeError

    # Check if the old and new password are not the same
    if verify_password(new_password.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="New password cannot be same as old password",
        )
    new_password.password = get_password_hash(new_password.password)

    # update the password of the current user
    update_result = await db["users"].update_one(
        {"_id": user["_id"]}, {"$set": new_password.dict()}
    )
    if update_result.modified_count == 1:
        updated_user = await db["users"].find_one({"_id": user["_id"]})

    existing_user = await db["users"].find_one({"_id": user["_id"]})
    if existing_user is not None or updated_user is not None:
        return {"msg": "Password updated successfully"}

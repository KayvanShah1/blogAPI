from fastapi import HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from fastapi import status

from app.core.jwt import verify_access_token
from app.db.database import db

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/api/v1/login/access-token")


async def get_current_user(token: str = Security(reusable_oauth2)):
    current_user_id = verify_access_token(token=token).id
    current_user = await db["users"].find_one({"_id": current_user_id})
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return current_user

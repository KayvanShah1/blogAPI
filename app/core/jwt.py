from datetime import datetime, timedelta

from jose import JWTError, jwt

from fastapi import HTTPException, status

from app.core import settings
from app.schemas.token import TokenData

access_token_jwt_subject = "access"
password_reset_request_subject = "password_reset_token"

credential_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not verify token, token expired",
    headers={
        "WWW-AUTHENTICATE": "Bearer",
    },
)


def create_access_token(
    payload: dict, expires_delta=settings.ACCESS_TOKEN_EXPIRE_MINUTES
):
    to_encode = payload.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def verify_access_token(token: str):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        id: str = payload.get("id")
        if not id:
            raise credential_exception
        token_data = TokenData(id=id)
        return token_data
    except JWTError:
        raise credential_exception

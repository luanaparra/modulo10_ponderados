from jose import jwt, JWTError
from fastapi import HTTPException, status, Depends
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
import models
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession


SECRET_KEY = "YOUR_SECRET_KEY"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") 
def create_access_token(user_id):
    print(user_id)
    claims = {
        "sub": str(user_id),
        "exp": datetime.utcnow() + timedelta(minutes=30)
    }
    return jwt.encode(claims, SECRET_KEY, algorithm=ALGORITHM)

async def authenticate_user(username: str, password: str, db):
    async with db as session:
        statement = select(models.User).where(models.User.username == username).limit(1)
        result = await session.execute(statement)
        user = result.scalars().first()
        print(user)
        if not user or user.password != password:
            return False
        return user

async def get_current_user(token: str, db) -> models.User:
    print(token)

    print('i will decode')
    payload = jwt.decode(token=token, key=SECRET_KEY, algorithms=ALGORITHM)
    print('i have decoded', payload)
    user_id: str = payload.get("sub")
    user_id = int(user_id)
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid JWT token")

    async with db as session:
        result = await session.execute(select(models.User).where(models.User.id == user_id))
        user = result.scalars().first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user

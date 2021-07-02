from typing import List

from fastapi import APIRouter

from models.user import User
from schemas.user import UserInDB, UserBase

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=List[UserInDB])
async def get_users():
    users = await User.all()
    return users


@router.post("/", response_model=UserInDB)
async def create_user(user_data: UserBase):
    user = await User.create(**user_data.dict())
    return user

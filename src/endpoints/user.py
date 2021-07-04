from typing import List

from fastapi import APIRouter

from models.user import User
from schemas.user import UserBase, UserOut

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=List[UserOut])
async def get_users():
    users = await User.all()
    return users


@router.post("/", response_model=UserOut)
async def create_user(user_data: UserBase):
    user = await User.create(**user_data.dict())
    return user

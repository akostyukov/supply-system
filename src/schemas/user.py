from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserOut(UserBase):
    id: int

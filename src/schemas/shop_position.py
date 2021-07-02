from decimal import Decimal

from pydantic import BaseModel


class ShopPositionBase(BaseModel):
    name: str
    price: Decimal


class ShopPositionInDB(ShopPositionBase):
    id: int

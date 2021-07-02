from typing import List

from fastapi import APIRouter

from models.shop_position import ShopPosition
from schemas.shop_position import ShopPositionInDB, ShopPositionBase

router = APIRouter(prefix="/shop", tags=["Shop"])


@router.get("/", response_model=List[ShopPositionInDB])
async def get_shop_positions():
    shop_positions = await ShopPosition.all()
    return shop_positions


@router.post("/")
async def create_shop_position(shop_position_data: ShopPositionBase):
    shop_position = await ShopPosition.create(**shop_position_data.dict())
    return shop_position

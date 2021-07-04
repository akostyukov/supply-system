from datetime import datetime
from decimal import Decimal
from typing import List

from pydantic import BaseModel

from schemas.shop_position import ShopPositionOut


class OrderBase(BaseModel):
    user_id: int
    shop_positions: List[int]


class OrderOut(OrderBase):
    id: int
    shop_positions: List[ShopPositionOut]
    datetime: datetime
    order_price: Decimal


class OrderMonthlyReport(BaseModel):
    user_id: int
    month: int
    summary_order_price: Decimal
    orders: List[OrderOut]

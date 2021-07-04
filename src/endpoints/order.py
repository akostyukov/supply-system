from typing import List

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from models.order import Order
from models.shop_position import ShopPosition
from schemas.order import OrderBase, OrderMonthlyReport, OrderOut

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.get("/{user_id}", response_model=List[OrderOut])
async def get_orders(user_id: int):
    orders = await Order.filter(user_id=user_id).prefetch_related("shop_positions")

    return [
        OrderOut(**jsonable_encoder(order), shop_positions=[*order.shop_positions])
        for order in orders
    ]


@router.get("/monthly-report/{user_id}", response_model=OrderMonthlyReport)
async def get_monthly_report(user_id: int, month: int):
    orders = await Order.filter(user_id=user_id).prefetch_related("shop_positions")
    orders = [order for order in orders if order.datetime.month == month]

    summary_order_price = 0

    for order in orders:
        summary_order_price += order.order_price

    return OrderMonthlyReport(
        user_id=user_id,
        month=month,
        summary_order_price=summary_order_price,
        orders=[
            OrderOut(**jsonable_encoder(order), shop_positions=[*order.shop_positions])
            for order in orders
        ],
    )


@router.get("/{user_id}/{order_id}", response_model=OrderOut)
async def get_order(user_id: int, order_id: int):
    order = await Order.get_or_none(id=order_id, user_id=user_id).prefetch_related(
        "shop_positions"
    )

    return OrderOut(**jsonable_encoder(order), shop_positions=[*order.shop_positions])


@router.post("/", response_model=OrderOut)
async def create_order(order_data: OrderBase):
    shop_positions_by_user = await ShopPosition.filter(id__in=order_data.shop_positions)
    order_price = 0

    for shop_position in shop_positions_by_user:
        order_price += shop_position.price

    order = await Order.create(user_id=order_data.user_id, order_price=order_price)
    await order.shop_positions.add(*shop_positions_by_user)

    return OrderOut(**jsonable_encoder(order), shop_positions=[*shop_positions_by_user])

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from db import TORTOISE_ORM
from endpoints import order, shop_position, user

app = FastAPI()

app.include_router(user.router)
app.include_router(shop_position.router)
app.include_router(order.router)

register_tortoise(app, TORTOISE_ORM, generate_schemas=True)

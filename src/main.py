from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from db import TORTOISE_ORM
from endpoints import order, shop_position, user

app = FastAPI()

routers = [user.router, shop_position.router, order.router]

for router in routers:
    app.include_router(router)

register_tortoise(app, TORTOISE_ORM, generate_schemas=True)

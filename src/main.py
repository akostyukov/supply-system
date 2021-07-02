from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from endpoints import user, shop_position
from db import TORTOISE_ORM

app = FastAPI()

app.include_router(user.router)
app.include_router(shop_position.router)

register_tortoise(app, TORTOISE_ORM, generate_schemas=True)

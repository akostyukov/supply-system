from tortoise import fields, models


class Order(models.Model):
    user = fields.ForeignKeyField("models.User")
    shop_positions = fields.ManyToManyField(
        "models.ShopPosition", related_name="shop_positions"
    )
    order_price = fields.DecimalField(max_digits=5, decimal_places=2)
    datetime = fields.DatetimeField(auto_now_add=True)

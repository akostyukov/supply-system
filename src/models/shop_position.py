from tortoise import fields, models


class ShopPosition(models.Model):
    name = fields.CharField(max_length=100)
    price = fields.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price} ₽"

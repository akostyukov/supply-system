from tortoise import fields, models


class User(models.Model):
    username = fields.CharField(max_length=50)

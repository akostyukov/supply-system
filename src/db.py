TORTOISE_ORM = {
    "connections": {"default": "postgres://postgres:postgres@localhost:5432/postgres"},
    "apps": {
        "models": {
            "models": ["models.user", "models.shop_position", "models.order"],
            "default_connection": "default",
        },
    },
}

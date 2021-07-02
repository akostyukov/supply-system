TORTOISE_ORM = {
    "connections": {"default": "sqlite://../db.sqlite"},
    # "connections": {"default": "postgres://postgres:postgres@db:5432/postgres"},
    "apps": {
        "models": {
            "models": ["models.user", "models.shop_position"],
            "default_connection": "default",
        },
    },
}

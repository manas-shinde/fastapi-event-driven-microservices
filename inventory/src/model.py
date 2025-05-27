from redis_om import HashModel
from src.redisDb import redis_db


class Product(HashModel):
    name: str
    quantity: int
    price: float

    class Meta:
        database: redis_db

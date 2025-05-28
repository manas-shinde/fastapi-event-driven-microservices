from redis_om import HashModel
from src.redis_db import REDIS_DB


class Order(HashModel):
    product_id: str
    price: float
    fee: float
    total_amout: float
    quantity: int
    status: str

    class Meta:
        database: REDIS_DB

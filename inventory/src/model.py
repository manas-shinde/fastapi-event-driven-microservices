from redis_om import HashModel, Field
from src.redis_db import REDIS_DB


class Product(HashModel):
    id: str = Field(index=True)
    name: str
    quantity: int
    unit_price: float

    class Meta:
        database: REDIS_DB

from pydantic import BaseModel


class Product(BaseModel):
    product_id: str
    product_name: str
    quantity: int
    unit_price: float

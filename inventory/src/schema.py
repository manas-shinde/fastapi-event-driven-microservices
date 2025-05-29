from pydantic import BaseModel


class CreateProductSchema(BaseModel):
    name: str
    quantity: int
    unit_price: float

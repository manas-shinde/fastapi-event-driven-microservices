from pydantic import BaseModel


class CreateProductSchema(BaseModel):
    name: str
    quantity: int
    price: float

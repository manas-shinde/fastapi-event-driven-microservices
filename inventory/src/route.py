from fastapi.exceptions import HTTPException
from fastapi import APIRouter, status
from redis_om import NotFoundError
from typing import List

from src.schema import CreateProductSchema
from src.model import Product
from src.utils import format_product

product_route = APIRouter()


@product_route.get("/", status_code=status.HTTP_200_OK)
async def get_all_products() -> List[Product]:
    return [format_product(pk) for pk in Product.all_pks()]


@product_route.get("/{id}")
def get_product_info(id: str) -> Product:
    try:
        all_products = list(Product.all_pks())
        for pk in all_products:
            prod = Product.get(pk)
            if prod.id == id:
                return prod

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product not found with id {id}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Exception occurred: {str(e)}"
        )


@product_route.post("/", status_code=status.HTTP_201_CREATED)
async def create_a_product(product: CreateProductSchema) -> Product:
    product_redis = Product(
        id=str(hash(product.name)),
        name=product.name,
        price=product.price,
        quantity=product.quantity
    )

    return product_redis.save()


@product_route.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_product(id: str):
    try:
        all_products = list(Product.all_pks())
        for pk in all_products:
            prod = Product.get(pk)
            if prod.id == id:
                Product.delete(pk)
                return {"message": f"Product with id {id} delete successfully!"}

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product not found with id {id}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Exception occurred: {str(e)}"
        )

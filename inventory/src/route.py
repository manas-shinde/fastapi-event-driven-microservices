from fastapi.exceptions import HTTPException
from fastapi import APIRouter, status
from redis_om import NotFoundError
from src.model import Product
from typing import List

product_route = APIRouter()


def format_product(pk: str):
    product = Product.get(pk)
    return {
        'id': product.pk,
        'name': product.name,
        'price': product.price,
        "quantity": product.quantity
    }


@product_route.get("/", status_code=status.HTTP_200_OK)
async def get_all_products() -> List[Product]:
    return [format_product(pk) for pk in Product.all_pks()]


@product_route.post("/", status_code=status.HTTP_201_CREATED)
async def create_a_product(product: Product) -> Product:
    return product.save()


@product_route.delete("/{pk}", status_code=status.HTTP_200_OK)
async def delete_product(pk: str):
    if Product.delete(pk):
        return {"message": f"Product with {pk} deleted successfully!"}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Product not found with id {pk}"
        )


@product_route.get("/{pk}")
async def get_product_info(pk: str) -> Product:
    try:
        return Product.get(pk)
    except NotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Product not found with id {pk}"
        )
    except Exception as e:
        return {"Exception Occured": e}

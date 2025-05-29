from fastapi import APIRouter, BackgroundTasks, status
from fastapi.requests import Request
from fastapi.exceptions import HTTPException
import requests

from src.utils import format_product, order_completed
from src.model import Order


PRODUCT_URL = "http://127.0.0.1:8001/api/v1/products"

order_route = APIRouter()


@order_route.get("/")
async def list_all_orders():
    return [format_product(pk) for pk in Order.all_pks()]


@order_route.get("/{pk}", status_code=status.HTTP_200_OK)
async def get_order(pk: str):
    try:
        return Order.get(pk)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product not found with id {id}"
        )


@order_route.post("/", status_code=status.HTTP_201_CREATED)
async def create_order(request: Request, background_tasks: BackgroundTasks):
    # request body contains only id and quantity of product
    body = await request.json()

    res = requests.get(
        f"{PRODUCT_URL}/{body['id']}")

    product = res.json()

    if int(product['quantity']) > int(body['quantity']):
        order = Order(
            product_id=product['id'],
            product_name=product['name'],
            unit_price=product['unit_price'],
            fee=0.2 * product['unit_price'],
            total_amout=(1.2 * product['unit_price'])*body['quantity'],
            quantity=body['quantity'],
            status="pending"
        )
        order.save()

        background_tasks.add_task(order_completed, order)

        return order
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Currenlty inventory dont have product name - {product['name']} with quantity - {body['quantity']} is not available."
        )

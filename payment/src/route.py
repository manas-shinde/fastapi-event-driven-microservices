from fastapi import APIRouter, BackgroundTasks
from fastapi.requests import Request
import requests

from src.utils import format_product, order_completed
from src.model import Order


PRODUCT_URL = "http://127.0.0.1:8001/api/v1/products"

order_route = APIRouter()


@order_route.get("/")
async def list_all_orders():
    return [format_product(pk) for pk in Order.all_pks()]


@order_route.get("/{pk}")
async def get_order(pk: str):
    return Order.get(pk)


@order_route.post("/")
async def create_order(request: Request, background_tasks: BackgroundTasks):
    # request body contains only id and quantity of product
    body = await request.json()

    res = requests.get(
        f"{PRODUCT_URL}/{body['id']}")

    product = res.json()

    order = Order(
        product_id=product['id'],
        price=product['price'],
        fee=0.2 * product['price'],
        total_amout=1.2 * product['price'],
        quantity=body['quantity'],
        status="pending"
    )
    order.save()

    background_tasks.add_task(order_completed, order)

    return order

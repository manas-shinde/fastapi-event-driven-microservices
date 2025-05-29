import time

from src.model import Order
from src.redis_db import REDIS_DB


def format_product(pk: str):
    order = Order.get(pk)
    return {
        "id": order.pk,
        'product_id': order.product_id,
        'unit_price': order.unit_price,
        'fee': order.fee,
        "quantity": order.quantity,
        "total_amout": order.total_amout,
        "status": order.status
    }


def order_completed(order: Order) -> None:
    time.sleep(5)
    order.status = "completed"
    order.save()
    print("send data in stream")
    REDIS_DB.xadd('order_completed', order.model_dump(), '*')

import time
from src.model import Order


def format_product(pk: str):
    order = Order.get(pk)
    return {
        "id": order.pk,
        'product_id': order.product_id,
        'price': order.price,
        'fee': order.fee,
        "quantity": order.quantity,
        "total_amout": order.total_amout,
        "status": order.status
    }


def order_completed(order: Order) -> None:
    time.sleep(5)
    order.status = "completed"
    order.save()

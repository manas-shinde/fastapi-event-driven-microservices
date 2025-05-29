import time
import json
import requests
from src.redis_db import REDIS_DB
from src.route import get_product_info
from src.model import Product


key = "order_completed"
group = "inventory-group"
UPDATE_ANALYTICS_URL: str = "http://127.0.0.1:8003/api/v1/analytics/update"


def consume_order_complete():
    try:
        REDIS_DB.xgroup_create(key, group)
    except:
        print(f"Group - {group} already exists!")

    while True:
        try:
            results = REDIS_DB.xreadgroup(group, key, {key: '>'}, None)
            if results != []:
                for result in results:
                    order = result[1][0][1]
                    product: Product = get_product_info(order['product_id'])
                    product.quantity = int(
                        product.quantity) - int(order['quantity'])
                    product.save()

                    # Update Analytics dataset
                    payload = json.dumps({
                        "product_id": product.id,
                        "product_name": product.name,
                        "quantity": int(order['quantity']),
                        "unit_price": product.unit_price
                    })
                    headers = {
                        'Content-Type': 'application/json'
                    }

                    response = requests.request(
                        "POST", UPDATE_ANALYTICS_URL, headers=headers, data=payload)

        except Exception as e:
            print(str(e))
            REDIS_DB.xadd("refund_order", order, '*')

        time.sleep(2)


if __name__ == "__main__":
    consume_order_complete()

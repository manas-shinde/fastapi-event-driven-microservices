import time
from src.redis_db import REDIS_DB
from src.model import Order


key = "refund_order"
group = "payment-group"


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
                    object = result[1][0][1]
                    order: Order = Order.get(object['pk'])
                    order.status = "refunded"
                    order.save()

        except Exception as e:
            print(str(e))

        time.sleep(2)


if __name__ == "__main__":
    consume_order_complete()

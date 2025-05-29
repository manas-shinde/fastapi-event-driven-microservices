from fastapi import APIRouter, Query
from src.redis_db import REDIS_DB
from src.schema import Product
analytics_routes = APIRouter()


@analytics_routes.post("/update")
def update_analytics(product: Product):
    product = product.model_dump()

    # Sales count per product
    REDIS_DB.incrby(
        f"analytics:sales:{product['product_id']}", product['quantity'])

    # Add to revenue
    total_price = product['quantity'] * product['unit_price']
    REDIS_DB.incrbyfloat("analytics:revenue", total_price)

    # Track popularity
    REDIS_DB.zincrby("analytics:popularity",
                     product['quantity'], product['product_name'])
    return {"status": "ok"}


@analytics_routes.get("/sales")
def get_sales():
    keys = REDIS_DB.keys("analytics:sales:*")
    return {k.split(":")[-1]: int(REDIS_DB.get(k)) for k in keys}


@analytics_routes.get("/revenue")
def get_revenue():
    return {"revenue": float(REDIS_DB.get("analytics:revenue") or 0)}


@analytics_routes.get("/popular-products")
def get_top_products(limit: int = Query(5)):
    return REDIS_DB.zrevrange("analytics:popularity", 0, limit - 1, withscores=True)

from src.model import Product


def format_product(pk: str):
    product = Product.get(pk)
    return {
        'id': product.id,
        'name': product.name,
        'price': product.price,
        "quantity": product.quantity
    }

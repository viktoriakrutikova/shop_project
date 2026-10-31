from eshop.models.customer import Customer
from eshop.models.product import Product

class Order:
    def __init__(self, order_id: int, customer: Customer, product: Product, count: int):
        self.order_id = order_id
        self.customer = customer
        self.product = product
        self.count = count
        self.total_price = product.price * count

    def to_dict(self) -> dict:
        return {
            "order_id": self.order_id,
            "customer_id": self.customer.customer_id,
            "product_id": self.product.product_id,
            "count": self.count,
            "total_price": self.total_price
        }
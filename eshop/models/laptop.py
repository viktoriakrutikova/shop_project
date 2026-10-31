from eshop.models.product import Product

class Laptop(Product):
    def __init__(self, product_id: int, name: str, price: float, quantity: int, cpu: str):
        super().__init__(product_id, name, price, quantity)
        self.cpu = cpu

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "Laptop"
        data["cpu"] = self.cpu
        return data
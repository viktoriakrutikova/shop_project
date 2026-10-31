from eshop.models.product import Product

class Smartphone(Product):
    def __init__(self, product_id: int, name: str, price: float, quantity: int, ram_gb: int):
        super().__init__(product_id, name, price, quantity)
        self.ram_gb = ram_gb

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "Smartphone"
        data["ram_gb"] = self.ram_gb
        return data
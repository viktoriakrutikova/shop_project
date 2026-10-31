from eshop.models.product import Product

class Headphones(Product):
    def __init__(self, product_id: int, name: str, price: float, quantity: int, is_wireless: bool):
        super().__init__(product_id, name, price, quantity)
        self.is_wireless = is_wireless

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "Headphones"
        data["is_wireless"] = self.is_wireless
        return data
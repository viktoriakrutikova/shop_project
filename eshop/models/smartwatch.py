from eshop.models.product import Product

class SmartWatch(Product):
    def __init__(self, product_id: int, name: str, price: float, quantity: int, strap_type: str):
        super().__init__(product_id, name, price, quantity)
        self.strap_type = strap_type

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "SmartWatch"
        data["strap_type"] = self.strap_type
        return data
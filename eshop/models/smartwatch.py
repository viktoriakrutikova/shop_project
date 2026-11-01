from eshop.models.product import Product

class Smartwatch(Product):
    def __init__(self, product_id: int, name: str, price: float, quantity: int, strap_material: str):
        super().__init__(product_id, name, price, quantity)
        self.strap_material = strap_material

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "Smartwatch"
        data["strap_material"] = self.strap_material
        return data
from eshop.models.product import Product

class Smartwatch(Product):
    """Класс Умные часы."""
    
    def __init__(self, product_id: int, name: str, price: float, quantity: int, strap_material: str):
        super().__init__(product_id, name, price, quantity)
        self.strap_material = strap_material
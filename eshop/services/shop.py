from typing import List
from eshop.models.product import Product
from eshop.exceptions.price_error import PriceError
from eshop.exceptions.not_found_error import NotFoundError

class ShopService:
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        if product.price <= 0:
            raise PriceError("Цена должна быть больше нуля!")
        if product.quantity < 0:
            raise PriceError("Количество не может быть отрицательным!")
        self.products.append(product)

    def get_all(self) -> List[Product]:
        return self.products

    def get_by_id(self, product_id: int) -> Product:
        for p in self.products:
            if p.product_id == product_id:
                return p
        raise NotFoundError(f"Товар с ID {product_id} не найден.")

    def update_price(self, product_id: int, new_price: float) -> None:
        product = self.get_by_id(product_id)
        if new_price <= 0:
            raise PriceError("Цена должна быть больше нуля!")
        product.price = new_price

    def delete_product(self, product_id: int) -> None:
        product = self.get_by_id(product_id)
        self.products.remove(product)
import json
from eshop.exceptions.shop_error import ShopError

class JSONStorage:
    def __init__(self, filename: str = "products.json"):
        self.filename = filename

    def save_products(self, products: list) -> None:
        try:
            data = [p.to_dict() for p in products]
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            raise ShopError(f"Не удалось сохранить JSON: {e}")

    def load_products(self) -> list:
        try:
            with open(self.filename, "r", encoding="utf-8-sig") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except Exception as e:
            raise ShopError(f"Не удалось прочитать JSON: {e}")
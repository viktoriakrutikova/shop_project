from eshop.exceptions.shop_error import ShopError

class NotFoundError(ShopError):
    """Ошибка, если объект не найден."""
    pass
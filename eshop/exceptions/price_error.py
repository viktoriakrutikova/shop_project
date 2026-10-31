from eshop.exceptions.shop_error import ShopError

class PriceError(ShopError):
    """Ошибка при неверно указанной цене или количестве."""
    pass
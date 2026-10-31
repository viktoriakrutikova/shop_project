from eshop.services.shop import ShopService
from eshop.models.product import Product
from eshop.models.smartphone import Smartphone
from eshop.models.laptop import Laptop
from eshop.models.headphones import Headphones
from eshop.models.smartwatch import Smartwatch
from eshop.storage.json_storage import JSONStorage
from eshop.storage.xml_storage import XMLStorage
from eshop.exceptions.shop_error import ShopError

def recreate_product(d):
    if not isinstance(d, dict):
        return d
    p_id = int(d.get("product_id", d.get("id", 0)))
    name = d.get("name", "")
    price = float(d.get("price", 0.0))
    qty = int(d.get("quantity", 0))
    
    if "ram" in d:
        return Smartphone(p_id, name, price, qty, int(d["ram"]))
    elif "cpu" in d:
        return Laptop(p_id, name, price, qty, str(d["cpu"]))
    elif "is_wireless" in d:
        val = d["is_wireless"]
        if isinstance(val, str):
            is_w = val.lower() in ("true", "да", "1", "yes")
        else:
            is_w = bool(val)
        return Headphones(p_id, name, price, qty, is_w)
    elif "strap_material" in d:
        return Smartwatch(p_id, name, price, qty, str(d["strap_material"]))
    else:
        return Product(p_id, name, price, qty)

def main():
    shop = ShopService()
    json_db = JSONStorage("shop_data.json")
    xml_db = XMLStorage("shop_data.xml")

    while True:
        print("\nМеню магазина")
        print("1. Показать список товаров")
        print("2. Добавить смартфон")
        print("3. Добавить ноутбук")
        print("4. Добавить наушники")
        print("5. Добавить умные часы")
        print("6. Обновить цену товара")
        print("7. Удалить товар")
        print("8. Сохранить в JSON")
        print("9. Загрузить из JSON")
        print("10. Сохранить в XML")
        print("11. Загрузить из XML")
        print("0. Выход")

        choice = input("Выберите пункт меню: ")

        try:
            if choice == "1":
                products = shop.get_all()
                if not products:
                    print("Список товаров пуст.")
                for p in products:
                    print(f"[{p.__class__.__name__}] ID: {p.product_id} | {p.name} | Цена: {p.price} руб. | Кол-во: {p.quantity} шт.")

            elif choice == "2":
                prod_id = int(input("Введите ID: "))
                name = input("Введите название: ")
                price = float(input("Введите цену: "))
                qty = int(input("Введите количество: "))
                ram = int(input("Объем ОЗУ (ГБ): "))
                
                phone = Smartphone(prod_id, name, price, qty, ram)
                shop.add_product(phone)
                print("Смартфон успешно добавлен")

            elif choice == "3":
                prod_id = int(input("Введите ID: "))
                name = input("Введите название: ")
                price = float(input("Введите цену: "))
                qty = int(input("Введите количество: "))
                cpu = input("Процессор: ")
                
                laptop = Laptop(prod_id, name, price, qty, cpu)
                shop.add_product(laptop)
                print("Ноутбук успешно добавлен")

            elif choice == "4":
                prod_id = int(input("Введите ID: "))
                name = input("Введите название: ")
                price = float(input("Введите цену: "))
                qty = int(input("Введите количество: "))
                is_wireless_input = input("Беспроводные? (да/нет): ").strip().lower()
                is_wireless = is_wireless_input in ("да", "y", "yes")
                
                headphones = Headphones(prod_id, name, price, qty, is_wireless)
                shop.add_product(headphones)
                print("Наушники успешно добавлены")

            elif choice == "5":
                prod_id = int(input("Введите ID: "))
                name = input("Введите название: ")
                price = float(input("Введите цену: "))
                qty = int(input("Введите количество: "))
                strap = input("Материал ремешка: ")
                
                smartwatch = Smartwatch(prod_id, name, price, qty, strap)
                shop.add_product(smartwatch)
                print("Умные часы успешно добавлены")

            elif choice == "6":
                prod_id = int(input("ID товара для изменения цены: "))
                new_price = float(input("Новая цена: "))
                shop.update_price(prod_id, new_price)
                print("Цена обновлена")

            elif choice == "7":
                prod_id = int(input("ID товара для удаления: "))
                shop.delete_product(prod_id)
                print("Товар удален")

            elif choice == "8":
                json_db.save_products(shop.get_all())
                print("Данные сохранены в JSON")

            elif choice == "9":
                raw_data = json_db.load_products()
                shop.products.clear()
                for item in raw_data:
                    shop.add_product(recreate_product(item))
                print(f"Загружено из JSON записей: {len(raw_data)}")

            elif choice == "10":
                xml_db.save_products(shop.get_all())
                print("Данные сохранены в XML")

            elif choice == "11":
                raw_data = xml_db.load_products()
                shop.products.clear()
                for item in raw_data:
                    shop.add_product(recreate_product(item))
                print(f"Загружено из XML записей: {len(raw_data)}")

            elif choice == "0":
                print("Выход из программы")
                break
            else:
                print("Неверный выбор, попробуйте от 0 до 11")

        except ShopError as err:
            print(f"[Ошибка магазина]: {err}")
        except ValueError:
            print("[Ошибка ввода]: Введите корректное число")
        except Exception as e:
            print(f"[Непредвиденная ошибка]: {e}")

if __name__ == "__main__":
    main()
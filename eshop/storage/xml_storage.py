import xml.etree.ElementTree as ET
from eshop.exceptions.shop_error import ShopError

class XMLStorage:
    def __init__(self, filename: str = "products.xml"):
        self.filename = filename

    def save_products(self, products: list) -> None:
        try:
            root = ET.Element("ProductsList")
            for p in products:
                prod_elem = ET.SubElement(root, "Product")
                for key, val in p.to_dict().items():
                    child = ET.SubElement(prod_elem, key)
                    child.text = str(val)

            tree = ET.ElementTree(root)
            tree.write(self.filename, encoding="utf-8", xml_declaration=True)
        except Exception as e:
            raise ShopError(f"Не удалось сохранить XML: {e}")

    def load_products(self) -> list:
        try:
            tree = ET.parse(self.filename)
            root = tree.getroot()
            result = []
            for item in root.findall("Product"):
                p_data = {}
                for child in item:
                    p_data[child.tag] = child.text
                result.append(p_data)
            return result
        except FileNotFoundError:
            return []
        except Exception as e:
            raise ShopError(f"Не удалось прочитать XML: {e}")
class ProductsPayloadBuilder:
    def __init__(self):
        self.__payload = {}

    def set_product_name(self, product_name: str):
        self.__payload["name"] = product_name
        return self

    def set_product_attributes(self, color: str, size: list[int] = None):
        product_attributes = {}
        product_attributes["color"] = color
        if size:
            product_attributes["size"] = size
        self.__payload["attributes"] = product_attributes
        return self

    def build(self):
        return self.__payload

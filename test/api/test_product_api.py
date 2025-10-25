from src.api.api_clients.product_client import ProductClient


class TestProductApi:
    def setup_class(self):
        self.product_client = ProductClient()

    def test_get_products(self):
        self.product_client.get_products()

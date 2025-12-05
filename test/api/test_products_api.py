import pytest

from src.api.api_clients.products_client import ProductClient


class TestProductsApi:
    def setup_class(self):
        self.product_client = ProductClient()

    def test_get_products(self):
        self.product_client.get_products()

    @pytest.mark.rate_limit
    def test_get_products_rate_limit(self):
        self.product_client.get_products()

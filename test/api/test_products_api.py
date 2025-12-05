import pytest

from src.api.api_assertions.api_assertions import ApiAssertions
from src.api.api_clients.products_client import ProductClient
from src.api.api_models.products_schema import products_schema
from src.common.log_utils import logger


class TestProductsApi:
    def setup_class(self):
        self.__product_client = ProductClient()
        self.__api_assertions = ApiAssertions()

    def test_get_products(self):
        logger().info("Getting products")
        self.__product_client.get_products()

    def test_get_products_schema(self):
        logger().info("Asserting products schema")
        response = self.__product_client.get_products()
        self.__api_assertions.assert_schema(response=response, schema=products_schema)

    @pytest.mark.rate_limit
    def test_get_products_rate_limit(self):
        logger().info("Asserting products rate limit")
        self.__product_client.get_products()

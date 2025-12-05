import pytest

from src.api.api_assertions.api_assertions import ApiAssertions
from src.api.api_clients.products_client import ProductsClient
from src.api.api_models.products_payload_builder import ProductsPayloadBuilder
from src.api.api_models.products_schema import products_schema
from src.common.log_utils import logger


class TestProductsApi:
    def setup_class(self):
        self.__products_client = ProductsClient()
        self.__api_assertions = ApiAssertions()
        self.__products_payload = ProductsPayloadBuilder()

    def test_get_products_api(self):
        logger().info("Getting products")
        self.__products_client.get_products()

    def test_get_products_by_category_api(self):
        logger().info("Getting products by category")
        self.__products_client.get_products(query_params={"category": "electronics"})

    def test_get_products_schema_api(self):
        logger().info("Asserting products schema")
        response = self.__products_client.get_products()
        self.__api_assertions.assert_schema(response=response, schema=products_schema)

    def test_add_product_api(self):
        logger().info("Adding product")
        self.__products_client.add_product(
            payload=self.__products_payload.set_product_name("Table")
            .set_product_attributes(color="red", size=[10, 12])
            .build()
        )

        logger().info("Adding product without size")
        self.__products_client.add_product(
            payload=self.__products_payload.set_product_name("Chair").set_product_attributes(color="blue").build()
        )

    @pytest.mark.rate_limit
    def test_get_products_rate_limit(self):
        logger().info("Asserting products rate limit")
        self.__products_client.get_products()

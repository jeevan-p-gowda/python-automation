import json

import pytest

from src.common.log_utils import logger
from src.ui.ui_assertions.products_ui_assertions import ProductsUiAssertions
from src.ui.ui_assertions.ui_assertions import UiAssertions
from src.ui.ui_page_objects.home_page import HomePage
from src.ui.ui_page_objects.products_page import ProductsPage


class TestProductsUi:
    @pytest.fixture(scope="function")
    def home_page(self, page):
        """Initialize the Home page with authenticated page."""
        return HomePage(page)

    @pytest.fixture(scope="function")
    def products_page(self, page):
        """Initialize the Products page with authenticated page."""
        return ProductsPage(page)

    @pytest.fixture(scope="function")
    def ui_assertions(self):
        """Initialize the UI assertions."""
        return UiAssertions()

    @pytest.fixture(scope="function")
    def products_ui_assertions(self):
        """Initialize the Products UI assertions."""
        return ProductsUiAssertions()

    @pytest.fixture(scope="function")
    def products_data(self):
        """Initialize the Products data."""
        return json.load(open("src/ui/ui_resources/products_data.json"))

    @pytest.fixture(autouse=True)
    def navigate_to_products_page(self, home_page):
        """Navigate to products page before each test."""
        home_page.navigate_to_products_page()

    def test_search_for_product_with_soft_assertion(self, products_page, products_ui_assertions, products_data):
        try:
            logger().info("Searching for product")
            products_page.search_for_product(product_name=products_data["product"]["productName"])

            logger().info("Asserting search results heading")
            products_ui_assertions.assert_search_results_heading(
                locator=products_page.get_search_results_heading(), soft=True
            )
        except Exception as e:
            logger().error(f"Exception: {e}")
            products_ui_assertions._exceptions.append(e)
        finally:
            pytest.fail(f"Exceptions: {products_ui_assertions._exceptions}") if len(
                products_ui_assertions._exceptions
            ) > 0 else None

    def test_search_for_product_with_hard_assertion(self, products_page, products_ui_assertions, products_data):
        logger().info("Searching for product")
        products_page.search_for_product(product_name=products_data["product"]["productName"])

        logger().info("Asserting search results heading")
        products_ui_assertions.assert_search_results_heading(locator=products_page.get_search_results_heading())

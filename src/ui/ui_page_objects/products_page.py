from playwright.sync_api import Page

from src.common.log_utils import log


class ProductsPage:
    def __init__(self, __page: Page):
        self.__page = __page
        self.__search_icon = __page.get_by_role("button", name="Search")
        self.__search_field = __page.get_by_placeholder("Search")
        self.__search_results_heading = __page.get_by_role("heading", name="Search results")

    @log
    def search_for_product(self, product_name: str):
        self.__search_icon.click()
        self.__search_field.fill(product_name)
        self.__search_field.press("Enter")

    @log
    def get_search_results_heading(self):
        return self.__search_results_heading

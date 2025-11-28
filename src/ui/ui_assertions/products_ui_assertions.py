from playwright.sync_api import Locator

from src.common.log_utils import log
from src.ui.ui_assertions.ui_assertions import UiAssertions


class ProductsUiAssertions(UiAssertions):
    def __init__(self):
        super().__init__()

    @log
    def assert_search_results_heading(self, locator: Locator, soft: bool = False):
        heading: str = "Search results"
        if soft:
            self.assert_text_in_an_element(locator=locator, text=heading, soft=True)
        else:
            self.assert_text_in_an_element(locator=locator, text=heading)

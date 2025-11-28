from playwright.sync_api import Page

from src.common.log_utils import log


class HomePage:
    def __init__(self, __page: Page):
        self.__page = __page
        self.__home_icon = __page.locator("//span[.='Home']")
        self.__account_icon = __page.get_by_role("link", name="Log in")

    @log
    def navigate_to_products_page(self):
        self.__home_icon.click()

    @log
    def navigate_to_login_page(self):
        self.__account_icon.click()

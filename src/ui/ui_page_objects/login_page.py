import pyotp
from playwright.sync_api import Page

from src.common.log_utils import log


class LoginPage:
    def __init__(self, __page: Page):
        self.__page = __page
        self.__email_field = __page.locator("#username")

    @log
    def login(self, email: str, password: str, totp: pyotp.TOTP):
        self.__email_field.click()
        self.__email_field.fill(email)
        self.__page.get_by_role("button", name="Sign In").click()
        self.__page.get_by_role("button", name="Continue").click()
        self.__page.get_by_role("textbox", name="Password").click()
        self.__page.get_by_role("textbox", name="Password").fill(password)
        self.__page.get_by_role("button", name="Log in").click()
        self.__page.get_by_role("textbox", name="Enter Code").click()
        self.__page.get_by_role("textbox", name="Enter Code").fill(totp.now())
        self.__page.get_by_role("button", name="Verify").click()
        self.__page.wait_for_timeout(10000)

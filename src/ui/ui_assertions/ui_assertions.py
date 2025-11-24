from playwright.sync_api import Locator, expect

from src.common.log_utils import log, logger


class UiAssertions:
    def __init__(self):
        self._exceptions = []

    @log
    def assert_visibility_of_element(self, locator: Locator, soft: bool = False):
        """Assert that a locator is visible with optional soft assertion."""
        if soft:
            try:
                expect(locator).to_be_visible()
            except AssertionError as e:
                logger().warning(f"Soft assertion failed: {locator} not visible - {e}")
                self._exceptions.append(e)
        else:
            expect(locator).to_be_visible()

    @log
    def assert_invisibility_of_element(self, locator: Locator, soft: bool = False):
        """Assert that a locator is invisible with optional soft assertion."""
        if soft:
            try:
                expect(locator).not_to_be_visible()
            except AssertionError as e:
                logger().warning(f"Soft assertion failed: {locator} is visible - {e}")
                self._exceptions.append(e)
        else:
            expect(locator).not_to_be_visible()

    @log
    def assert_text_in_an_element(self, locator: Locator, text: str, soft: bool = False):
        """Assert that a locator contains text."""
        if soft:
            try:
                expect(locator).to_contain_text(text)
            except AssertionError as e:
                logger().warning(f"Soft assertion failed: {locator} does not contain '{text}' - {e}")
                self._exceptions.append(e)
        else:
            expect(locator).to_contain_text(text)

    @log
    def assert_contains_class_in_an_element(self, locator: Locator, class_attribute_value: str, soft: bool = False):
        if soft:
            try:
                expect(locator).to_contain_class(class_attribute_value)
            except AssertionError as e:
                logger().warning(
                    f"Soft assertion failed: {locator} does not contain class '{class_attribute_value}' - {e}"
                )
                self._exceptions.append(e)
        else:
            expect(locator).to_contain_class(class_attribute_value)

    @log
    def assert_not_contains_class_in_an_element(self, locator: Locator, class_attribute_value: str, soft: bool = False):
        if soft:
            try:
                expect(locator).not_to_contain_class(class_attribute_value)
            except AssertionError as e:
                logger().warning(f"Soft assertion failed: {locator} contains class '{class_attribute_value}' - {e}")
                self._exceptions.append(e)
        else:
            expect(locator).not_to_contain_class(class_attribute_value)

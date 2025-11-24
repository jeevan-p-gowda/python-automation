import pytest
from playwright.sync_api import expect

from src.common.common_utils import check_and_load_env
from src.common.env_enums import EnvEnums
from src.common.log_utils import logger
from src.ui.ui_page_objects.login_page import LoginPage


@pytest.fixture(scope="session", autouse=True)
def create_ui_session(request, playwright):
    """
    Create a UI session and login to the application.
    """
    from src.ui.ui_utils.otp_auth import totp

    logger().info("Loading env variables...")
    env: str = request.config.getoption("--env")
    env_vars = check_and_load_env(env=env)

    logger().info("--Executing global setup--")
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()

    logger().info("Navigating to base URL...")
    page.goto(env_vars[EnvEnums.BASE_URL.value])
    login_page = LoginPage(page)

    logger().info("Logging into the application...")
    login_page.login(
        email=env_vars[EnvEnums.EMAIL.value],
        password=env_vars[EnvEnums.PASSWORD.value],
        totp=totp(env_vars[EnvEnums.MFA_SECRET_KEY.value]),
    )

    logger().info("Setting storage state...")
    context.storage_state(path=f".auth/{env}-auth.json")  # noqa: F821
    browser.close()
    logger().info("--Global setup completed 🌐--")


@pytest.fixture(scope="class")
def page(browser, request):
    """
    Navigate to the base URL with storage state.
    """
    env: str = request.config.getoption("--env")
    context = browser.new_context(storage_state=f".auth/{env}-auth.json")
    page = context.new_page()
    # Navigation timeout
    page.set_default_navigation_timeout(50000)
    # Action timeout
    page.set_default_timeout(50000)
    # Assertion timeout
    expect.set_options(timeout=15000)

    env_vars = check_and_load_env(env=env)
    logger().info("Navigating to base URL with storage state...")
    page.goto(env_vars[EnvEnums.BASE_URL.value])
    yield page
    browser.close()

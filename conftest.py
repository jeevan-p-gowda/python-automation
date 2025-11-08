import time

import pytest

from src.api.api_clients.auth_client import AuthClient
from src.common.common_utils import check_and_load_env
from src.common.log_utils import logger, set_logger


def pytest_addoption(parser):
    parser.addoption("--env", action="store", required=True, help="Environment to run tests on")


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Dynamically configure pytest options based on conditions."""

    is_ui_test = any("tests/ui" in str(arg) for arg in config.args)
    is_api_test = any("tests/api" in str(arg) for arg in config.args)

    if is_ui_test:
        config.option.xmlpath = "results/ui/junit.xml"
        config.option.htmlpath = "results/ui/report.html"
    elif is_api_test:
        config.option.xmlpath = "results/api/junit.xml"
        config.option.htmlpath = "results/api/report.html"
    else:
        raise ValueError("Invalid test path. Expected /ui or /api in path.")


@pytest.fixture(scope="session", autouse=True)
def create_api_session(request) -> None:
    """Create a session for the test."""
    set_logger(request.config.args[0])

    env: str = request.config.getoption("--env")
    env_vars = check_and_load_env(env=env)
    auth_client = AuthClient(**env_vars)
    auth_client.create_api_session()
    yield
    auth_client.teardown_api_session()


@pytest.fixture(scope="function", autouse=True)
def log_test_start_end_time(request):
    """Automatically log the start and end time of each test."""
    test_name = request.node.name
    logger().info(f"Starting test: {test_name}")
    start_time = time.time()
    yield
    end_time = time.time()
    duration = end_time - start_time
    logger().info(f"Finished test: {test_name} in {duration:.2f} seconds")

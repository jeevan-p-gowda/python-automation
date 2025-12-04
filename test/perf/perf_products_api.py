import json

from locust import HttpUser, between, events, task

from src.api.api_clients.auth_client import AuthClient
from src.api.api_constants.api_enums import EndpointEnums
from src.common.common_utils import check_and_load_env
from src.common.env_enums import EnvEnums

test_stats = None
env_vars = None
endpoints = json.load(open(EndpointEnums.ENDPOINT_JSON_PATH.value))


@events.init_command_line_parser.add_listener
def _(parser):
    parser.add_argument("--env", type=str, required=True, help="Environment to run tests against (e.g., int, prod)")


@events.init.add_listener
def _(environment, **kwargs):
    """Load environment variables and set up global configurations."""
    global env_vars

    # Get the --env from cli
    env_name = environment.parsed_options.env

    env_vars = check_and_load_env(env=env_name)

    # Set host on RttUser class before users are spawned
    ProductsUser.host = env_vars.get(EnvEnums.API_URL.value)


@events.test_stopping.add_listener
def _(environment, **kwargs):
    """Capture performance stats before test ends."""
    global test_stats

    # Get runtime from environment stats for header
    total_stats = environment.stats.total
    test_stats = {
        "run_duration": total_stats.last_request_timestamp - total_stats.start_time if total_stats.start_time else 0,
        "concurrent_users": environment.runner.user_count if hasattr(environment.runner, "user_count") else 0,
        "apis": [],
    }

    for name, stats in environment.stats.entries.items():
        if stats.method:  # Skip aggregated entries
            # Extract just the path from the name (in case it's a tuple)
            api_path = name[0] if isinstance(name, tuple) else name
            test_stats["apis"].append(
                {
                    "method": stats.method,
                    "api": api_path,
                    "percentile_95": stats.get_response_time_percentile(0.95),
                    "average_response_time": stats.avg_response_time,
                    "num_requests": stats.num_requests,
                    "num_failures": stats.num_failures,
                    "rps": round(stats.total_rps, 2),
                }
            )


@events.quitting.add_listener
def _(environment, **kwargs):
    """Capture performance stats after test ends."""
    global test_stats
    if test_stats:
        print(json.dumps(test_stats, indent=4))


class ProductsUser(HttpUser):
    """Client Side Performance Test for products endpoint."""

    host = None  # Will be set from env_vars in @events.init
    wait_time = between(0.1, 0.5)  # Wait 0.1-0.5 seconds between tasks for better coverage
    connection_timeout = 30.0  # 30 second connection timeout
    network_timeout = 30.0  # 30 second read timeout

    def on_start(self):
        global env_vars, endpoints
        self.__endpoints = endpoints
        # Set authentication token
        auth_client = AuthClient(**env_vars)
        self.__token = auth_client.get_bearer_token()
        self.client.headers.update({"Authorization": f"Bearer {self.__token}"})

    @task
    def get_products(self):
        """Client Side Performance Test products endpoint."""
        with self.client.get(
            self.__endpoints["product"]["products"],
            name=f"GET {self.__endpoints['product']['products']}",
            catch_response=True,
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Status: {response.status_code}")

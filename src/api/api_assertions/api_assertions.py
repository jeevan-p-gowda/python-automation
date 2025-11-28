from jsonschema import validate

from src.common.assertions import Assertions


class ApiAssertions(Assertions):
    def __init__(self):
        super().__init__()

    def assert_method_not_allowed(self, response, soft: bool = False):
        self.assert_value_equals(expected_value="Method not allowed", actual_value=response["error"], soft=soft)

    def assert_options_headers(self, response, soft: bool = False):
        self.assert_value_equals(
            expected_value="GET, OPTIONS", actual_value=response["Access-Control-Allow-Methods"], soft=soft
        )

    def assert_schema(self, response, schema):
        validate(instance=response, schema=schema)

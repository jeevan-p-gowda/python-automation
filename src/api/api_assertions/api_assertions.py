from jsonschema import validate

from src.common.assertions import Assertions


class ApiAssertions(Assertions):
    def __init__(self):
        super().__init__()

    def assert_method_not_allowed(self, response):
        self.assert_value_equals("Method not allowed", response["error"])

    def assert_options_headers(self, response):
        self.assert_value_equals("GET, OPTIONS", response["Access-Control-Allow-Methods"])

    def assert_schema(self, response, schema):
        validate(instance=response, schema=schema)

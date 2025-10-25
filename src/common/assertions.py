from src.common.log_utils import log


class Assertions:
    def __init__(self):
        pass

    @log
    def assert_value_equals(self, expected_value, actual_value):
        assert expected_value == actual_value

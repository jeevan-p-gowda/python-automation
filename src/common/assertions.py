from src.common.log_utils import log, logger


class Assertions:
    def __init__(self):
        self._exceptions = []

    @log
    def assert_value_equals(self, expected_value, actual_value, soft: bool = False):
        if soft:
            try:
                assert expected_value == actual_value
            except AssertionError as e:
                logger().warning(f"Soft assertion failed: {expected_value} != {actual_value} - {e}")
                self._exceptions.append(e)
        else:
            assert expected_value == actual_value

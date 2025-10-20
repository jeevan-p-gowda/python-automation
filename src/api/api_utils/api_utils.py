import re

from src.common.log_utils import log


class ApiUtils:
    def __init__(self):
        pass

    @log
    def build_api(self, api_url: str, endpoint: str, **kwargs) -> str:
        api: str = endpoint

        # Extract all placeholders from the endpoint string
        placeholders = re.findall(r"\{([^}]+)\}", endpoint)

        # Check if all placeholders have corresponding kwargs
        missing_params = [param for param in placeholders if param not in kwargs]
        if missing_params:
            raise ValueError(f"Missing required parameters: {missing_params} in {api}")

        # Replace placeholders with actual values
        for param in placeholders:
            api = api.replace(f"{{{param}}}", str(kwargs.pop(param)))

        kwargs.update({"url": api_url + api})
        return kwargs

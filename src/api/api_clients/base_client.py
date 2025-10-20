import json

import requests
from src.api.api_constants.api_enums import EndpointEnums
from src.api.api_utils.api_utils import ApiUtils
from src.common.log_utils import pretty_print_request_and_response


class _BaseClient:
    api_url: str = None
    org_id: str = None
    session: requests.Session = None
    endpoints: dict = json.load(open(EndpointEnums.ENDPOINT_JSON_PATH.value))

    def __init__(self):
        self.api_utils = ApiUtils()
        self.endpoint_str: str = EndpointEnums.ENDPOINT_STR.value

    def get(self, **kwargs) -> str:
        api: dict = self.api_utils.build_api(
            api_url=self.api_url, endpoint=kwargs.pop(self.endpoint_str), **kwargs
        )
        response: requests.Response = self.session.get(**api)
        pretty_print_request_and_response(response)
        response.raise_for_status()
        return json.loads(response.text)

    def post(self, **kwargs) -> str:
        api: dict = self.api_utils.build_api(
            api_url=self.api_url, endpoint=kwargs.pop(self.endpoint_str), **kwargs
        )
        response: requests.Response = self.session.post(**api)
        pretty_print_request_and_response(response)
        # response.raise_for_status()
        return json.loads(response.text)

    def put(self, **kwargs) -> str:
        api: dict = self.api_utils.build_api(
            api_url=self.api_url, endpoint=kwargs.pop(self.endpoint_str), **kwargs
        )
        response: requests.Response = self.session.put(**api)
        pretty_print_request_and_response(response)
        response.raise_for_status()
        return json.loads(response.text)

    def delete(self, **kwargs) -> str:
        api: dict = self.api_utils.build_api(
            api_url=self.api_url, endpoint=kwargs.pop(self.endpoint_str), **kwargs
        )
        response: requests.Response = self.session.delete(**api)
        pretty_print_request_and_response(response)
        response.raise_for_status()
        return json.loads(response.text)

    def options(self, **kwargs) -> str:
        api: dict = self.api_utils.build_api(
            api_url=self.api_url, endpoint=kwargs.pop(self.endpoint_str), **kwargs
        )
        response: requests.Response = self.session.options(**api)
        pretty_print_request_and_response(response)
        response.raise_for_status()
        return response.headers

import base64
import json

import requests
from src.api.api_clients.base_client import _BaseClient
from src.common.env_enums import EnvEnums
from src.common.log_utils import log, logger


class AuthClient(_BaseClient):
    def __init__(self, **kwargs):
        super().__init__()
        self.__requests = requests
        self.__auth_url = kwargs.pop(EnvEnums.AUTH_URL.value)
        self.__api_key = kwargs.pop(EnvEnums.API_KEY.value)
        self.__api_secret = kwargs.pop(EnvEnums.API_SECRET.value)
        self.__api_url = kwargs.pop(EnvEnums.API_URL.value)
        self.__org_id = kwargs.pop(EnvEnums.ORG_ID.value)

    @log
    def get_bearer_token(self):
        credentials = base64.b64encode(
            (self.__api_key + ":" + self.__api_secret).encode()
        ).decode("utf-8")
        response = self.__requests.get(
            self.__auth_url,
            headers={"Authorization": f"Basic {credentials}"},
        )
        response.raise_for_status()
        return json.loads(response.text)["access_token"]

    @log
    def create_api_session(self):
        access_token: str = self.get_bearer_token()
        self.__session = requests.Session()
        self.__session.headers.update(
            {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {access_token}",
            }
        )
        logger().info("Setting session...")
        _BaseClient.session = self.__session
        _BaseClient.api_url = self.__api_url
        _BaseClient.org_id = self.__org_id

    @log
    def teardown_api_session(self):
        self.__session.close()

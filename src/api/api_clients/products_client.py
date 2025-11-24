from src.api.api_clients.base_client import _BaseClient
from src.common.log_utils import log


class ProductsClient(_BaseClient):
    def __init__(self, **kwargs):
        super().__init__()

    @log
    def get_products(self):
        return self.get(endpoint=self.endpoints["product"]["products"])

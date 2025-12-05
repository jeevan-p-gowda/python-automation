from src.api.api_clients.base_client import _BaseClient
from src.common.log_utils import log


class ProductsClient(_BaseClient):
    def __init__(self, **kwargs):
        super().__init__()

    @log
    def get_products(self, query_params: dict | None = {"category": str} | None):
        return self.get(endpoint=self.endpoints["product"]["products"], params=query_params)

    @log
    def add_product(self, payload: dict):
        return self.post(endpoint=self.endpoints["product"]["products"], json=payload)

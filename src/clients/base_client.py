import requests

from src.core.settings import (
    BASE_URL,
    DEFAULT_TIMEOUT,
)


class BaseClient:

    def __init__(self):
        self.session = requests.Session()
        self.base_url = BASE_URL

    def get(self, endpoint: str):
        return self.session.get(
            f"{self.base_url}{endpoint}",
            timeout=DEFAULT_TIMEOUT,
        )

    def post(self, endpoint: str, **kwargs):
        return self.session.post(
            f"{self.base_url}{endpoint}",
            timeout=DEFAULT_TIMEOUT,
            **kwargs,
        )

    def put(self, endpoint: str, **kwargs):
        return self.session.put(
            f"{self.base_url}{endpoint}",
            timeout=DEFAULT_TIMEOUT,
            **kwargs,
        )

    def delete(self, endpoint: str):
        return self.session.delete(
            f"{self.base_url}{endpoint}",
            timeout=DEFAULT_TIMEOUT,
        )

from asyncio import timeout

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



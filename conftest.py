import pytest

from src.clients.product_client import ProductsClient


@pytest.fixture(scope="session")
def products_client():
    return ProductsClient()
import pytest

from src.clients.product_client import ProductsClient


@pytest.fixture
def products_client():
    return ProductsClient()
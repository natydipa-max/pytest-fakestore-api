#DELETE
from src.models.product_model import ProductModel


def test_delete_product(products_client):
    response = products_client.delete_product(1)

    assert response.status_code == 200

    deleted = ProductModel.model_validate(
            response.json())

    assert deleted.id == 1
#PUT
from src.models.product_request_model import ProductRequestModel
from src.models.product_response_model import ProductResponseModel


def test_update_product(products_client):
    product = ProductRequestModel(
        title="Updated Product",
        price=0.99,
        description="Updated Product Description",
        category="testing",
        image="https://example.com/image.jpg",
    )

    response = products_client.update_product(1, product)

    assert response.status_code == 200

    updated = ProductResponseModel.model_validate(
        response.json()
    )

    assert updated.title == product.title
    assert updated.price == product.price
    assert updated.description == product.description
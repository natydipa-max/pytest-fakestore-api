#POST
from src.models.product_request_model import ProductRequestModel
from src.models.product_response_model import ProductResponseModel


def test_create_product(products_client):
    product = ProductRequestModel(
        title="Test Product",
        price=10.99,
        description="Test Description",
        category="electronics",
        image="https://example.com/image.jpg",
    )

    response = products_client.create_product(product)

    assert response.status_code == 201

    created = ProductResponseModel.model_validate(
        response.json()
    )

    assert created.title == product.title
    assert created.price == product.price

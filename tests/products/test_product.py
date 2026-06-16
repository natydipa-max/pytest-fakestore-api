from src.models.product_response_model import ProductResponseModel
from src.models.product_model import ProductModel
from src.models.product_request_model import ProductRequestModel

# GET
def test_get_product_by_id(products_client):

    response = products_client.get_product(1)

    assert response.status_code == 200

    product = ProductModel.model_validate(
        response.json()
    )
    assert product.id == 1

def test_get_all_products(products_client):
    response = products_client.get_all_products()

    assert response.status_code == 200

    products = [
        ProductModel.model_validate(product)
        for product in response.json()
   ]

    assert len(products) > 0

#POST
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

    created_product = ProductResponseModel.model_validate(
        response.json()
    )

    assert created_product.title == product.title
    assert created_product.price == product.price

#PUT
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

    updated_product = ProductResponseModel.model_validate(
        response.json()
    )

    assert updated_product.title == product.title
    assert updated_product.price == product.price
    assert updated_product.description == product.description

#DELETE
def test_delete_product(products_client):
    response = products_client.delete_product(1)

    assert response.status_code == 200

    deleted_product = ProductModel.model_validate(
        response.json()
    )

    assert deleted_product.id == 1
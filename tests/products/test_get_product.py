def test_get_product_by_id(products_client):

    response = products_client.get_product(1)

    assert response.status_code == 200

    product = response.json()

    assert product["id"] == 1
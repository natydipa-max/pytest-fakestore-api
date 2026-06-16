

# Fake Store API only returns 400 for malformed JSON payloads.
# Business validation errors are not implemented by the API.

def test_create_product_with_malformed_json_returns_400(products_client):
    response = products_client.session.post(
        f"{products_client.base_url}/products",
        data='{"title":"Test","price":}',
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 400
    assert "Bad Request" in response.text

def test_update_product_with_malformed_json_returns_400(products_client):
    response = products_client.session.put(
            f"{products_client.base_url}/products/1",
            data='{"title":"Test","price":}',
            headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 400
    assert "Bad Request" in response.text
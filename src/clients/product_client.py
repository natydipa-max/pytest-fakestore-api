from src.clients.base_client import BaseClient
from src.models.product_response_model import ProductResponseModel

class ProductsClient(BaseClient):

    def get_all_products(self):
        return self.get("/products")

    def get_product(self, product_id: int):
        return self.get(f"/products/{product_id}")

    def create_product(self, product: ProductResponseModel):
        return self.post(
            "/products",
            json=product.model_dump())

    def update_product(self, product_id: int, product: ProductResponseModel):
        return self.put(f"/products/{product_id}",
                        json=product.model_dump())

    def delete_product(self, product_id: int):
        return self.delete(f"/products/{product_id}")



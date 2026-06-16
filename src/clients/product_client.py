from src.clients.base_client import BaseClient


class ProductsClient(BaseClient):

    def get_all_products(self):
        return self.get("/products")

    def get_product(self, product_id: int):
        return self.get(f"/products/{product_id}")



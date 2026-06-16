from src.models.product_model import BaseModel

class ProductResponseModel(BaseModel):
    id: int
    title: str
    price: float
    description: str
    category: str
    image: str

from pydantic import BaseModel

from src.models.rating_model import RatingModel


class ProductModel(BaseModel):
    id: int
    title: str
    price: float
    description: str
    category: str
    image: str
    rating: RatingModel
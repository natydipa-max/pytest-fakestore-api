from pydantic import BaseModel

class ProductRequestModel(BaseModel):
    title: str
    price: float
    description: str
    category: str
    image: str
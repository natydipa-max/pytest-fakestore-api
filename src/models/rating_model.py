from pydantic import BaseModel

class RatingModel(BaseModel):
    rate: float
    count: int
    
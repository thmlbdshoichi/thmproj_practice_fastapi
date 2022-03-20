from pydantic import BaseModel

class Movie(BaseModel):
    title: str
    type: str
    score: float
    price: float
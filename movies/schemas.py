from pydantic import BaseModel
from typing import Optional

class Movie(BaseModel):
    title: str
    genre: str
    score: float
    price: float
    release: Optional[bool] = None
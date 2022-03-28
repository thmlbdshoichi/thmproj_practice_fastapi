from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from .database import Base

class Movie(Base):
    __tablename__ = "moviesCatalog"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    genre = Column(String)
    score = Column(Float)
    price = Column(Float)
    release = Column(Boolean, default=False)
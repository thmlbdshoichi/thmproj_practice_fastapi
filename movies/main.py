from typing import Optional
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import database, models, schemas

app = FastAPI()
models.Base.metadata.create_all(database.engine)

# SQL DATABASE
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ROUTE PART
@app.post('/movies')
async def create(request:schemas.Movie, db: Session = Depends(get_db)):
    new_movie = models.Movie(
        title=request.title,
        genre=request.genre,
        score=request.score,
        price=request.price,
        release=request.release
    )
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie
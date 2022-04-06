from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import Response, JSONResponse
from sqlalchemy.orm import Session
from typing import Optional, List
from . import auth
from .. import database, models, schemas

###########################################################################
router = APIRouter(
    prefix="/movies",
    tags=['Movies']
)
###########################################################################

@router.post('/', status_code=201)
async def create(request:schemas.Movie, db: Session = Depends(database.get_db)):
    new_movie = models.Movie(
        title=request.title,
        genre=request.genre,
        score=request.score,
        price=request.price,
        release=request.release,
        seller_uid=request.seller_uid
    )
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie

@router.get('/', status_code=200, response_model=List[schemas.showMovie])
async def findAll(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(auth.get_current_user)):
    movies = db.query(models.Movie).all()
    return movies

@router.get('/{id}', status_code=200, response_model=schemas.showMovie)
async def findOne(id: int, db: Session = Depends(database.get_db)):
    movie = db.query(models.Movie).filter(models.Movie.id == id).first()
    if movie is None:
        raise HTTPException(status_code=404, detail="Specific Movie not found")
    return movie

@router.delete('/{id}')
async def destroy(id: int, db: Session = Depends(database.get_db)):
    movie = db.query(models.Movie).filter(models.Movie.id == id)
    if movie.first() is None:
        raise HTTPException(status_code=404, detail="Specific Movie not found so it is not deleted.")
    movie.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.patch('/{id}')
async def update(id: int, request: schemas.patchMovie, db: Session = Depends(database.get_db)):
    movie = db.query(models.Movie).filter(models.Movie.id == id)
    #request.score = 8.8
    if movie.first() is None:
        raise HTTPException(status_code=404, detail="Specific Movie not found so it is not updated.")
    movie.update(request.dict(exclude_unset=True))
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
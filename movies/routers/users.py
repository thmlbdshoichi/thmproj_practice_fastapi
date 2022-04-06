from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import Response, JSONResponse
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from typing import Optional, List
from .. import database, models, schemas

###########################################################################
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")
###########################################################################
router = APIRouter(
    prefix="/users",
    tags=['Users'],
)
###########################################################################
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.showUser)
async def create(request: schemas.User, db: Session = Depends(database.get_db)):
    hashedPassword = pwd_cxt.hash(request.password)
    new_user = models.User(
        username = request.username,
        password = hashedPassword,
        role = request.role
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return request

@router.get('/', status_code=200, response_model=List[schemas.showUser])
async def findAll(db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    return users

@router.get('/{username}', status_code=200, response_model=schemas.showUser)
async def findOne(username: str, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Can't find a specific user details")
    return user

@router.delete('/{username}')
async def destroy(username: str, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == username)
    if user.first() is None:
        raise HTTPException(status_code=404, detail="Can't find a specific user so it is not deleted.")
    user.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.patch('/{username}')
async def update(username: str, request: schemas.patchUser, db: Session = Depends(database.get_db)):
    if request.password:
        request.password = pwd_cxt.hash(request.password)
    user = db.query(models.User).filter(models.User.username == username)
    if user.first() is None:
        raise HTTPException(status_code=404, detail="Can't find a specific user so it is not updated.")
    user.update(request.dict(exclude_unset=True))
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
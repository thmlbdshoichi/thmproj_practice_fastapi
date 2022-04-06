from pydantic import BaseModel
from typing import Optional, List

## DEFAULT -- DATABASE
class User(BaseModel):
    username: str
    password: str
    role: str

class Movie(BaseModel):
    title: str
    genre: str
    score: float
    price: float
    release: bool
    seller_uid: str

# PATCH PYDANTIC
class patchUser(User):
    username: Optional[str]
    password: Optional[str]
    role: Optional[str]
    

class patchMovie(Movie):
    title: Optional[str]
    genre: Optional[str]
    score: Optional[float]
    price: Optional[float]
    release: Optional[bool]
    seller_uid: Optional[str]

# QUERY SHOW RELATION

class titleMovie(BaseModel):
    id: int
    title: str
    class Config():
        orm_mode = True

class usernameUser(BaseModel):
    username: str
    class Config():
        orm_mode = True
class showUser(BaseModel):
    username: str
    role: str
    resMovies: List[titleMovie] = []
    class Config():
        orm_mode = True
class showMovie(BaseModel):
    title: str
    genre: str
    score: float
    price: float
    seller_uid: str
    class Config():
        orm_mode = True
        
        
# USER AUTHENTICATION JWT SCHEMA
class authUser(BaseModel):
    username: str
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
    role: Optional[str] = None
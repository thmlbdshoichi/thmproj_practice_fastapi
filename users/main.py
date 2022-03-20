from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    password: str
    name: str
    role: str
    
    

@app.post('/users')
def create():
    return {"Details": "Hello Worlds!"}
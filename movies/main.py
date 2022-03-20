from fastapi import FastAPI
from . import schemas

app = FastAPI()

@app.post('/movies')
def create(request: schemas.Movie):
    return request
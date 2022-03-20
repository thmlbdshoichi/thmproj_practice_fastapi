from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/blog')
def get_all_blogs(limit:int=10, published:bool=False, sort:Optional[str]=None):
    if published:
        return {"data": f"{limit} published blogs from the db"}
    else:
        return {"data": f"{limit} blogs from the db"}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]=False

@app.post('/blog')
def create_blog(request: Blog):
    return request.title

#if __name__ == "__main__":
#    uvicorn.run(app, host="127.0.0.1", port=8000)
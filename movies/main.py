from typing import Optional, List
from fastapi import FastAPI
from . import database, models, schemas
from .routers import auth, movies, users

models.Base.metadata.create_all(database.engine)
##############################################################
# APP ROUTE
############################################################## 
app = FastAPI()
app.include_router(auth.router)
app.include_router(movies.router)
app.include_router(users.router)
##############################################################

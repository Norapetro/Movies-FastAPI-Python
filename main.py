from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from utils.jwt_manager import create_token
from config.database import  engine,Base
from models.movie import Movie as MovieModel
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router



app = FastAPI()
app.title = "Mi APP con FastAPI"

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)

  


movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": 2009,
        "rating": 7.8,
        "category": "Acción"
    },
        {
        "id": 2,
        "title": "Avatar2",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": 2023,
        "rating": 7.8,
        "category": "Acción"
    }
]

@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('<h1>Hola Bonita</h1>')



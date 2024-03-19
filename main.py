from fastapi import FastAPI
from database import User, Movie, UserReview
from database import database as conecction
from datetime import datetime
from schemas import UserRequestModel
from schemas import UserResponseModel
from fastapi import HTTPException

# uvicorn main:app --reload
app = FastAPI(tittle= "Proyecto para reseñar peliculas",
              version="1")


@app.on_event("startup")
def startup():
    if conecction.is_closed():
        conecction.connect()
        
    conecction.create_tables([User,Movie,UserReview])     
    
@app.on_event("shutdown")
def shutdown():
    if not conecction.is_closed():
        conecction.close()
       
        
@app.get("/")
async def index():
    return "Hola perro"


@app.post("/users", response_model=UserResponseModel)
async def create_user(user: UserRequestModel):
    
    if User.select().where(User.username == user.username).exists():
        return HTTPException(409, "El user ya existe")
    
    hash_password = User.create_password(user.password)
    
    user = User.create(
        username = user.username,
        password = hash_password,
    )
    
    return UserResponseModel(id=user.id, username=user.username)
    

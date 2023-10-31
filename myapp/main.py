from fastapi import FastAPI
from routers import users,authentication
from models import Base,Users
from database import engine

app = FastAPI()
app.include_router(authentication.router)
app.include_router(users.router)

Base.metadata.create_all(engine)


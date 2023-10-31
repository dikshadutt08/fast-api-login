from fastapi import APIRouter
import schema
from fastapi import FastAPI, Depends, status, Response, HTTPException
from schema import *
from schema import User
from models import Base,Users
from sqlalchemy.orm import Session
from database import get_db
from repository import users
import oauth2
from oauth2 import *

router=APIRouter(
    prefix="/user",
    tags=['Users']
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: User, db: Session = Depends(get_db)):
    return users.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    return users.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: User, db: Session = Depends(get_db)):
    return users.update(id, request, db)

@router.get('/',status_code=status.HTTP_200_OK)
def all(db: Session = Depends(get_db), get_current_user: schema.User= Depends(get_current_user)):
    return users.all(db)

@router.get('/{id}',status_code=200)
def show(id, db: Session = Depends(get_db)):
    return users.show(id,db)

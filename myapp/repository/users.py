from fastapi import FastAPI, Depends, status, Response, HTTPException
import schema
import models
from schema import *
from schema import User
from models import Base,Users
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash
from repository import users


def create(request: schema.User, db: Session):
    new_user = models.Users(
        name=request.username, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def destroy(id: int, db: Session = Depends(get_db)):
    user1=db.query(Users).filter(Users.id==id)
    if not user1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with id {id} is not available in the records!!')
    user1.delete(synchronize_session=False)
    db.commit()
    return "User has been deleted !!"

def update(id: int, request: User, db: Session = Depends(get_db)):
    appuser=db.query(Users).filter(Users.id==id)
    if not appuser.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'user with id {id} is not availaible in the Records !!')
    appuser.update({'name':request.username,'email':request.email,'password':Hash.bcrypt(request.password)})
    db.commit()
    return "Details have been Updated!"

def all(db: Session = Depends(get_db)):
    users= db.query(Users).all()
    return users

def show(id, db: Session = Depends(get_db)):
    my_user=db.query(Users).filter(Users.id == id).first()
    if not my_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with id {id} is not available in the records!!')
    return my_user
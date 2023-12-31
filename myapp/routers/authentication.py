from fastapi import APIRouter,status,HTTPException, Depends
from sqlalchemy.orm import Session
import database
import models
from models import Users
from hashing import Hash
import schema
from authtoken import *
from fastapi.security import OAuth2PasswordRequestForm
#from authtoken import create_token
from schema import *
router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm= Depends(), db: Session = Depends(database.get_db)):
    user=db.query(Users).filter(Users.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")
    
    access_token = create_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
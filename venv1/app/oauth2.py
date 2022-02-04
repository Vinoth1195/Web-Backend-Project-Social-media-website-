from email import header
from time import time
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from .databaseintialize import get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from datetime import datetime, timedelta
from . import models
from fastapi.security import OAuth2PasswordBearer
from . import schemas
from .config import settings


OAuth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict):
    to_encode = data.copy()
    expir = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"expires": str(expir)})
    token=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return token

def verify_access_token(token: str, credantials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        id: str= payload.get("userid")
        exp: str= payload.get("expires")
        if id is None or datetime.utcnow() > datetime.strptime(exp,'%Y-%m-%d %H:%M:%S.%f'):
            raise credantials_exception
        token_data=schemas.TokenData(id=id)
        if exp is None:
            raise credantials_exception
    except JWTError:
        raise credantials_exception
        
       
    return token_data

def fetch_user(token: str = Depends(OAuth2_scheme), db: Session = Depends(get_db)):
    
    credantials_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"could not validate credandials", headers={"WWW-Authenticate": "Bearer"})

    token_data= verify_access_token(token, credantials_exception)

 
    current_user = db.query(models.Users).filter(models.Users.id==token_data.id).first()

    return current_user
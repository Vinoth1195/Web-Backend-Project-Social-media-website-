from typing import List
from fastapi import APIRouter,Depends,HTTPException, Response, routing,status
from ..databaseintialize import get_db
from .. import schemas
from .. import models
from sqlalchemy.orm import Session
from .. import utils
from .. import oauth2
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
router = APIRouter()


@router.post("/login", status_code=status.HTTP_200_OK)
def login(user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    userinfo= db.query(models.Users).filter(models.Users.email==user.username).first()

    if not userinfo:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")


    elif not utils.verifypassword(user.password, userinfo.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

        
    else:
        token=oauth2.create_access_token({"userid":userinfo.id})
        return {"access_token":token, "token_type":"bearer"}
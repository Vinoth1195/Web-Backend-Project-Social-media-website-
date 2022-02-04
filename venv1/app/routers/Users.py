from fastapi import APIRouter,Depends,HTTPException, routing,status
import fastapi
from ..databaseintialize import get_db
from ..schemas import Users,UserCreated
from .. import models
from sqlalchemy.orm import Session
from ..utils import hashpassword, verifypassword
from .. import oauth2
router = APIRouter(prefix="/users")

@router.post("/create", response_model= UserCreated )
def createuser(user: Users, db: Session = Depends(get_db)):
    user.password= hashpassword(user.password)
    new_user=user.dict()
    newuser= models.Users(**new_user)
    db.add(newuser)
    db.commit()
    db.refresh(newuser)

    return newuser

@router.get("/", response_model=UserCreated)
def getuser(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.fetch_user)):
    user=db.query(models.Users).filter(models.Users.id==id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user id {id} does not exist")
    return user


        

from fastapi import APIRouter,Depends, FastAPI,HTTPException, routing,status
from sqlalchemy.orm import Session
from ..import schemas
from ..import models
from ..databaseintialize import get_db
from .. import oauth2

router=APIRouter(prefix="/vote")


@router.post("/")
def votes(uservote: schemas.Vote, db: Session = Depends(get_db), current_user: dict = Depends(oauth2.fetch_user)):
    query= db.query(models.Vote).filter(uservote.post_id==models.Vote.post_id, current_user.id == models.Vote.user_id)
    currentquery = query.first()
    
    if currentquery==None and uservote.dir==1:
        
        currentpost = db.query(models.Posts2).filter(uservote.post_id==models.Posts2.id).first()
        
        if currentpost == None:
            raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Post with id {uservote.post_id} does not exist")
        newvote=models.Vote(post_id=uservote.post_id, user_id= current_user.id)
        db.add(newvote)
        db.commit()
        return f"voted on post with id {uservote.post_id}"

    elif currentquery!=None and uservote.dir==1:
        raise HTTPException(status_code=status.HTTP_201_CREATED, detail=f"Already voted on post with id{uservote.post_id}")

    elif currentquery!=None and uservote.dir==0:
        print("hello")
        query.delete(synchronize_session=False)
        db.commit()
        return f"Post with id {uservote.post_id} is unvoted"

    elif currentquery==None and uservote.dir==0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Post with id {uservote.post_id} does not exist")
        


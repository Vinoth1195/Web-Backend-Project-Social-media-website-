from typing import List, Optional
from fastapi import APIRouter,Depends,HTTPException, Response, routing,status
from sqlalchemy import func
from ..databaseintialize import get_db
from ..schemas import Posts,ReturnPosts, ReturnAllPosts
from .. import models
from sqlalchemy.orm import Session
from .. import oauth2
router = APIRouter()





@router.get("/allposts", response_model= List[ReturnAllPosts])
def getposts2(db: Session = Depends(get_db), current_user: int = Depends(oauth2.fetch_user), limit: int = 3, skip: int= 0, search: Optional[str]="" ):
    allposts=db.query(models.Posts2, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Posts2.id == models.Vote.post_id, isouter=True).group_by(models.Posts2.id).filter(models.Posts2.title.contains(search)).limit(limit).offset(skip).all()
    return allposts


@router.post("/createpost", response_model= ReturnPosts)
def createpost(post: Posts, db: Session = Depends(get_db), current_user: int = Depends(oauth2.fetch_user)):
    # cursor.execute("""INSERT INTO "AllPosts" (title, content, published) values (%s,%s,%s) RETURNING * """,(post.title, post.content, post.published))
    # added_post=cursor.fetchone()
    # conn.commit()

    new_post=post.dict()
    newpost= models.Posts2(owner_id=current_user.id,**new_post)
    db.add(newpost)
    db.commit()
    db.refresh(newpost)

    return newpost
    

@router.get("/posts/{id}",response_model=ReturnAllPosts)
def getpost(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.fetch_user)):
    # cursor.execute("""SELECT * from "AllPosts" where id=%s""",(str(id)))
    # currentpost=cursor.fetchone()

    currentpost= db.query(models.Posts2, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Posts2.id == models.Vote.post_id, isouter=True).group_by(models.Posts2.id).filter(models.Posts2.id==id).first()


    if not currentpost:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post id {id} not found")
    return currentpost

@router.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def deletepost(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.fetch_user)):
    # cursor.execute("""DELETE from "AllPosts" where id=%s RETURNING *""",(str(id)))
    # deletedpost=cursor.fetchone()
    currentpost=db.query(models.Posts2).filter(models.Posts2.id==id).filter(models.Posts2.owner_id==current_user.id)
    
    if currentpost.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post id {id} does not exist")
    currentpost.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    
@router.patch("/posts/{id}")
def updatepost(post: Posts, id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.fetch_user)):
    # cursor.execute("""UPDATE "AllPosts" SET title=%s, content=%s, 
    # published=%s WHERE id=%s RETURNING *""",(post.title,post.content,post.published,str(id)))
    # updatedpost=cursor.fetchone()
    # conn.commit()
    updatedata=post.dict()
    currentpost=db.query(models.Posts2).filter(models.Posts2.id==id).filter(models.Posts2.owner_id==current_user.id)
    if currentpost.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post id {id} does not exist")
    currentpost.update(updatedata, synchronize_session=False)
    db.commit()
    return currentpost.first()
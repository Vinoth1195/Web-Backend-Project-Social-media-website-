
from fastapi import FastAPI
from . import models
from .databaseintialize import engine
from .routers import Posts, Users, Authentication, Votes
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI()

origins=["*"]
app.add_middleware(
     CORSMiddleware,
     allow_origins=origins,
     allow_credentials=True,
     allow_methods=["*"],
     allow_headers=["*"],
 )


app.include_router(Posts.router)
app.include_router(Users.router)
app.include_router(Authentication.router)
app.include_router(Votes.router)
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "hello - world"}


# @app.get("/allposts")
# def getallposts():
#     cursor.execute("""SELECT * FROM "AllPosts" """)
#     posts=cursor.fetchall()
#     return posts


                


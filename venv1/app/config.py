from os import environ
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE:str
    DBUSERNAME:str
    PASSWORD:str
    PORT:str
    DBSERVER:str
    SECRET_KEY:str
    ALGORITHM:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int

    class Config:
        env_file=".env"

settings = Settings()
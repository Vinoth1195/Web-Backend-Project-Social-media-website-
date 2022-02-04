from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashpassword(password):
    return pwd_context.hash(password)

def verifypassword(plainpassword, hashpassword):
    return pwd_context.verify(plainpassword,hashpassword)
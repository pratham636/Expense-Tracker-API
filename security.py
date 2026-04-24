import bcrypt
from jose import jwt
from datetime import datetime,timedelta
from fastapi import HTTPException
SECRET_KEY="mysecretkey"
ALGORITHM="HS256"

def hash_password(password:str)->str:
    try:
        password_bytes=password.encode("utf-8")
        salt=bcrypt.gensalt()
        hash_password1=bcrypt.hashpw(password_bytes,salt)
        return hash_password1.decode("utf-8") 
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Error in hashing password:{str(e)}")
def verify_password(hashed_password:str,password:str)->bool:
    try:
        password_bypes=password.encode("utf-8")
        hashed_password_bytes=hashed_password.encode("utf-8")
        return bcrypt.checkpw(password_bypes,hashed_password_bytes)
    except Exception as e:
        raise HTTPException(status_code=401,detail=f"Error in verifying password:{str(e)}")
       
def create_access_token(data:dict):
    try:
        to_encode=data.copy()
        expire=datetime.utcnow()+timedelta(minutes=30)
        to_encode.update({"exp":expire})
        token=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
        return token
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Error in creating access token : {str(e)}")
def verify_token(token:str):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except Exception as e:
        raise HTTPException(status_code=401,detail=f"Error in verifying token : {str(e)}")
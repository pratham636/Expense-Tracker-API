from fastapi import FastAPI, HTTPException,Depends,APIRouter
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from schemas import UserRegister , UserLogin , UserResponse,ExpenseCreate,ExpenseResponse
from security import hash_password,verify_password,create_access_token , verify_token
from database import engine,SessionLocal,Base
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse  
import models

router=APIRouter()
security=HTTPBearer()
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(credentials:HTTPAuthorizationCredentials=Depends(security)):
    try:
        token=credentials.credentials
        payload=verify_token(token)
        if payload is None:
            raise HTTPException(status_code=401,detail='Invalid token')
        return payload
    except Exception as e:
        print(f"Token verification failed {e}")
        raise HTTPException(status_code=401,detail='Could not validate credentials')


@router.post("/register")
def register_data(user:UserRegister,db:Session=Depends(get_db)):
    try:
        hashed_password=hash_password(user.password)
        new_users=models.Users(
            name=user.username,
            email=user.email,
            hash_password = hashed_password
        )
        db.add(new_users)
        db.commit()
        db.refresh(new_users)
        return {"message":'Registeration complited'}
    except Exception as e:
        raise HTTPException(status_code=401,detail=f'Enter the wrong credential  = {str(e)}')
@router.post("/login")
def login(user:UserLogin,db:Session=Depends(get_db)):
    new_email=user.email
    new_password=user.password
    try:
        data=db.query(models.Users).filter(models.Users.email==new_email).first()
        if data is None:
            raise HTTPException(status_code=404,detail="User not found")
        elif verify_password(data.hash_password,new_password):
                token=create_access_token(
                {"sub":data.email,
                 "id":data.id}
                )
                return {"access_token":token,"token_type":"bearer"}
        raise HTTPException(status_code=401,detail='Incorrect password')
    except Exception as e: 
        raise HTTPException(status_code=404,detail=f'Users not found.={str(e)}')

@router.post("/profile")
def get_profile(user=Depends(get_current_user)):
    try:
        if user is None:
            raise HTTPException(status_code=401,detail=f"Invalid authentication credential {str(e)}")    
        return {
                "message":"This is a protected route",
                "user_email":user.get("sub"),
                "user_id":user.get("id") 
            } 
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Internal serval error : {str(e)}")

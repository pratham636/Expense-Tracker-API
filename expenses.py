from fastapi import  HTTPException,Depends,APIRouter
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from schemas import UserRegister , UserLogin , UserResponse,ExpenseCreate,ExpenseResponse,ExpenseUpdate
from security import hash_password,verify_password,create_access_token,verify_token
from database import engine,SessionLocal
from sqlalchemy.orm import Session 
from schemas import ExpenseCreate,ExpenseResponse
from fastapi.responses import JSONResponse  
import models

router=APIRouter()
security=HTTPBearer()

def getdb():
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
        raise HTTPException(status_code=401,detail=f'Could not validate credentials {str(e)}')

@router.get("/expenses/view")
def expenses(db:Session=Depends(getdb)):
    try:
        data=db.query(models.Expenses).all()        
        if data is None:
            HTTPException(status_code=404,detail='Post is not found.')
        return data
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Internal serval error = {str(e)}")
@router.get("/expenses/view/{item_id}")
def expenses_id(item_id:int,db:Session=Depends(getdb)):
    try:
        data=db.query(models.Expenses).filter(models.Expenses.id==item_id).first()
        if data is None:
            raise HTTPException(status_code=404,detail='Post is not found.')
        return data
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Internal serval error = {str(e)}")
        

@router.post("/expenses/create")
def expenses_create(expenses:ExpenseCreate,db:Session=Depends(getdb),current_user: models.Users = Depends(get_current_user)):
    try:
        db_post=models.Expenses(title=expenses.title,
                                amount=expenses.amount,
                                category=expenses.category,
                                date=expenses.date,
                                user_id=current_user['id']) 
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        return {'message':'Item added successfully.'}
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Internal server error : {str(e)}")
    
@router.put("/expenses/update/{item_id}")
def expenses_update(item_id:int,creat:ExpenseUpdate, db:Session=Depends(getdb)):
    try:
        data=db.query(models.Expenses).filter(models.Expenses.id==item_id).first()        
        if data is None:
            raise HTTPException(status_code=404,detail='Patient not found')
        # existing_iteam_info = data.copy()
        updated_iteam_info=creat.model_dump(exclude_unset=True)
        for key , value in updated_iteam_info.items():
            setattr(data,key,value)
        db.commit()
        db.refresh(data)
        return {'message':'patient updated'}
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Internal server error : {str(e)}")
    

@router.delete("/expenses/delete/{item_id}")
def delete(item_id:int,db:Session=Depends(getdb)):
    try:
        data=db.query(models.Expenses).filter(models.Expenses.id==item_id).first()
        if data is None:
            raise HTTPException(status_code=404,detail='Item is not found.')
        db.delete(data)
        db.commit()
        return {'message':'Iteam deleted successfully.'}
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Internal server error : {str(e)}")
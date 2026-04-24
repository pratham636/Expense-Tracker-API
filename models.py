from sqlalchemy import BOOLEAN,Column,Integer,String,ForeignKey,Float,Date
from database import Base
class Users(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    name=Column(String(50),nullable=False)
    email=Column(String(50),nullable=False,unique=True)
    hash_password=Column(String(255),nullable=False)

class Expenses(Base):
    __tablename__='expenses'
    id=Column(Integer,index=True,autoincrement=True,primary_key=True)  
    title=Column(String(255),nullable=False)
    amount=Column(Float,nullable=False)
    category=Column(String(100),nullable=False)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    date=Column(Date, nullable=False)
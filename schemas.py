from pydantic import BaseModel , EmailStr , Field
from typing import List, Dict, Optional,Annotated

class UserRegister(BaseModel):
    username:Annotated[str,Field(title='Name of the user',description='Give the name of the user less than 50 character',examples=['Nitish'])]
    email:Annotated[EmailStr,Field(title='Email address',description='Give the email of the user less than 50 character',examples=['Josh@gmail.com'])]
    password:Annotated[str,Field(description='Enter the password')]

class UserLogin(BaseModel):
    email:Annotated[EmailStr,Field(description='Enter valid email')]
    password:Annotated[str,Field(description='Enter valid password')]

class UserResponse(BaseModel):
    id:Annotated[int,Field(description='Enter the id')]
    username:Annotated[str,Field(description='Enter the username')]
    email:Annotated[EmailStr,Field(description='Enter the email')]

class ExpenseCreate(BaseModel):
    title:Annotated[str,Field(description='Enter the title')]
    amount:Annotated[float,Field(description='Enter the amout',gt=0)]
    category:Annotated[str,Field(description='Enter the categoty')]
    date:Annotated[str,Field(description='Enter the date')]
class ExpenseResponse(BaseModel):
    id:Annotated[int,Field(description='Enter the id')]
    title:Annotated[str,Field(description='Enter the titel')]
    amount:Annotated[float,Field(description='Enter the amout',gt=0)]
    category:Annotated[str,Field(description='Enter the category')]
    date:Annotated[str,Field(description='Enter the date')]
    user_id:Annotated[int,Field(description='Enter the user_id')]

class ExpenseUpdate(BaseModel):
    title:Annotated[Optional[str],Field(default=None,description='Enter the titel')]
    amount:Annotated[Optional[float],Field(default=None,description='Enter the amout',gt=0)]
    category:Annotated[Optional[str],Field(default=None,description='Enter the categoty')] 
    date:Annotated[Optional[str],Field(default=None,description='Enter the date')]

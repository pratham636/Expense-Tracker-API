from fastapi import FastAPI
from database import engine,Base
import auth,expenses 


app=FastAPI() 
Base.metadata.create_all(bind=engine) 

app.include_router(auth.router)
app.include_router(expenses.router)
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

URL_DATABASE="mysql+pymysql://root:"your_password"@localhost:3306/expenses_tracker_api"
engine=create_engine(URL_DATABASE)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base() 
 

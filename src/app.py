from typing import Optional
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from .models import *


# database
DATABASE_URL = "sqlite:///db/storedb.db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind= engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)

# depenency to get the database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 


@app.get('/')
def read_root():
    return "Server is running"

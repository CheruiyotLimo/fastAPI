from typing import Optional, List

from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas, utilities
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import posts, users, auth
models.Base.metadata.create_all(bind=engine)

app = FastAPI()



while True:
    try:
        conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="password", cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Succesful connection.")
        break
    except Exception as error:
        print("Database connection failed")
        print(error)
        time.sleep(2)


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Hello World!!!"}


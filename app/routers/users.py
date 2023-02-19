from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, utilities
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserReturn)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hash_password = utilities.hash(user.password)
    user.password = hash_password
    new_user = models.User(**user.dict())
    user_check = db.query(models.User).filter(models.User.email == user.email).first()
    
    if user_check:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"User with email: {user.email} already exists.")
        
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return f"The acount was succesfully created"

@router.get("/{id}", response_model=schemas.UserReturn)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} not found.")
    return user
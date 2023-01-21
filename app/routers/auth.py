
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import database, schemas, models, utilities

router = APIRouter(tags=["Authentication"])

@router.post("/login")
def login(user_credetials: schemas.UserLogin, db: Session = Depends(database.get_db())):

    user = db.query(models.User).filter(models.User.email == user_credetials.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials")
    
    if not utilities.verify_password(user_credetials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials")
    

    return {"token": "example token"}
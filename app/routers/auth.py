
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import database, schemas, models, utilities, oauth2w
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=["Authentication"])

@router.post("/login", response_model=schemas.Token)
def login(user_credetials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

    user = db.query(models.User).filter(models.User.email == user_credetials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials")
    
    if not utilities.verify_password(user_credetials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials")
    
    access_token = oauth2w.create_access_token({"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}
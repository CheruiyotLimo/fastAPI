from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, oauth2w
from sqlalchemy.orm import Session
from ..database import get_db
from typing import Optional, List

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get("/", response_model=List[schemas.PostReturn])
def get_posts(db: Session = Depends(get_db), user_id: int = Depends(oauth2w.get_current_user)):
    posts = db.query(models.Post).all()
    print(user_id)
    print(posts)
    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostReturn)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), user_id: int = Depends(oauth2w.get_current_user)):
    new_post = models.Post(**post.dict())
    print(user_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/{id}", response_model=schemas.PostReturn)
def get_single_post(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2w.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    print(user_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found.")
    return post


@router.delete("/{id}")
def delete_post(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2w.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The post with id {id} does not exist.")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.PostReturn)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), user_id: int = Depends(oauth2w.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The post with id {id} does not exist.")
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()
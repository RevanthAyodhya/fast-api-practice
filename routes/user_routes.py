from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth import get_current_user, require_admin
from database import get_db
from models import User, UserDB
from services import user_service

router = APIRouter(prefix="/users")


@router.post("/")
def create_user(user: User, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)


@router.get("/users")
def get_users(
    db: Session = Depends(get_db),
    current_user: UserDB = Depends(get_current_user),
):
    print(current_user.email)
    return user_service.list_users(db)


@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.get_user(db, user_id)


@router.put("/{user_id}")
def update_user(user_id: int, updated_user: User, db: Session = Depends(get_db)):
    return user_service.update_user(db, user_id, updated_user)


@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: UserDB = Depends(require_admin),
):
    return user_service.delete_user(db, user_id)

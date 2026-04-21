from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import User
from services import user_service

router = APIRouter()


@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    return user_service.login_user(db, email, password)


@router.post("/register")
def register(user: User, db: Session = Depends(get_db)):
    return user_service.register_user(db, user)

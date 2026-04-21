from fastapi import HTTPException
from sqlalchemy.orm import Session

from auth import create_access_token, hash_password, verify_password
from models import User
from repositories import user_repo


def create_user(db: Session, user: User):
    return user_repo.create(
        db,
        name=user.name,
        age=user.age,
        email=user.email,
    )


def list_users(db: Session):
    return user_repo.get_all(db)


def get_user(db: Session, user_id: int):
    user = user_repo.get_by_id(db, user_id)
    if not user:
        return {"error": "User not found"}
    return user


def update_user(db: Session, user_id: int, updated_user: User):
    user = user_repo.get_by_id(db, user_id)
    if not user:
        return {"error": "User not found"}
    return user_repo.update(db, user, name=updated_user.name, age=updated_user.age)


def delete_user(db: Session, user_id: int):
    user = user_repo.get_by_id(db, user_id)
    if not user:
        return {"error": "User not found"}
    user_repo.delete(db, user)
    return {"message": "Deleted"}


def register_user(db: Session, user: User):
    hashed = hash_password(user.password)
    user_repo.create(
        db,
        name=user.name,
        age=user.age,
        email=user.email,
        password=hashed,
    )
    return {"message": "User created"}


def login_user(db: Session, email: str, password: str):
    user = user_repo.get_by_email(db, email)

    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    if not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Invalid password")

    token = create_access_token({"sub": user.email, "role": user.role})
    return {"access_token": token}

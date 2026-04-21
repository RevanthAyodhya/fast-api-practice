from sqlalchemy.orm import Session
from models import UserDB


def get_all(db: Session):
    return db.query(UserDB).all()


def get_by_id(db: Session, user_id: int):
    return db.query(UserDB).filter(UserDB.id == user_id).first()


def get_by_email(db: Session, email: str):
    return db.query(UserDB).filter(UserDB.email == email).first()


def create(db: Session, name: str, age: int, email: str, password: str | None = None):
    db_user = UserDB(
        name=name,
        age=age,
        email=email,
        password=password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update(db: Session, user: UserDB, name: str, age: int):
    user.name = name
    user.age = age
    db.commit()
    db.refresh(user)
    return user


def delete(db: Session, user: UserDB):
    db.delete(user)
    db.commit()

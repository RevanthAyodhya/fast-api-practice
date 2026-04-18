from fastapi import APIRouter,Depends
from models import User
from sqlalchemy.orm import Session
from database import get_db
from models import UserDB
router=APIRouter(prefix="/users")
# users=[]
# @router.post("/")
# def create_user(user:User):
#     users.append(user)
#     return {"message":"User added","data":user}

# @router.get("/users")
# def get_users():
#     return users

# @router.get("/{user_id}")
# def get_user(user_id:int):
#     for user in users:
#         if user.id==user_id:
#             return user
#     return{"error":"User not found"}


# @router.put("/{user_id}")
# def update_user(user_id:int, updated_user:User):
#     for i,user in enumerate(users):
#         if user.id==user_id:
#             users[i]=updated_user
#             return{"message":"User updated"}
#     return {"error":"User not found"}

# @router.delete("/{user_id}")
# def delete_user(user_id:int):
#     for i,user in enumerate(users):
#         if user.id==user_id:
#             users.pop(i)
#             return{"message":"User deleted"}
#     return {"error":"User not found"}


# @router.get("/users/db")
# def get_users():
#     db = SessionLocal()
#     users = db.query(UserDB).all()
#     db.close()
#     return users

@router.post("/users")
def create_user(user:User,db:Session=Depends(get_db)):
    # db=SessionLocal()
    db_user=UserDB(
        id=user.id,
        name=user.name,
        age=user.age
        email=user.email
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    # db.close()
    return db_user

@router.get('/users')
def get_users(db:Session=Depends(get_db)):
    # db=SessionLocal()
    users=db.query(UserDB).all()
    # db.close()
    return users

@router.get("/users/{user_id}")
def get_user(user_id: int,db:Session=Depends(get_db)):
    # db = SessionLocal()

    user = db.query(UserDB).filter(UserDB.id == user_id).first()

    # db.close()

    if not user:
        return {"error": "User not found"}

    return user


@router.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User,db:Session=Depends(get_db)):
    # db = SessionLocal()

    user = db.query(UserDB).filter(UserDB.id == user_id).first()

    if not user:
        # db.close()
        return {"error": "User not found"}

    user.name = updated_user.name
    user.age = updated_user.age

    db.commit()
    db.refresh(user)

    # db.close()

    return user


@router.delete("/users/{user_id}")
def delete_user(user_id: int,db:Session=Depends(get_db)):
    # db = SessionLocal()

    user = db.query(UserDB).filter(UserDB.id == user_id).first()

    if not user:
        # db.close()
        return {"error": "User not found"}

    db.delete(user)
    db.commit()

    # db.close()

    return {"message": "User deleted"}

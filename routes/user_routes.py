from fastapi import APIRouter
from models import User

router=APIRouter(prefix="/users")
users=[]
@router.post("/")
def create_user(user:User):
    users.append(user)
    return {"message":"User added","data":user}

@router.get("/users")
def get_users():
    return users

@router.get("/{user_id}")
def get_user(user_id:int):
    for user in users:
        if user.id==user_id:
            return user
    return{"error":"User not found"}


@router.put("/{user_id}")
def update_user(user_id:int, updated_user:User):
    for i,user in enumerate(users):
        if user.id==user_id:
            users[i]=updated_user
            return{"message":"User updated"}
    return {"error":"User not found"}

@router.delete("/{user_id}")
def delete_user(user_id:int):
    for i,user in enumerate(users):
        if user.id==user_id:
            users.pop(i)
            return{"message":"User deleted"}
    return {"error":"User not found"}
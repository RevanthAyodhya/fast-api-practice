from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
from routes.user_routes import router  as user_router
from routes.product_routes import router as product_router
from routes.auth_routes import router as auth_router
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (for now)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_router)
app.include_router(product_router)
app.include_router(auth_router)

# class User(BaseModel):
#     name:str
#     age:int


# class User(BaseModel):
#     id:int
#     name:str
#     age:int


users=[]

# @app.get("/")                       Lesson 1
# def read_root():
#     return {"Message":"Response from first api"}


# @app.get('/hello')
# def say_hello():
#     return {"Message":"Hello from another route"}


# @app.get('/users')                  Lesson 2
# def get_users():
#     return ['user1','user2','user3']


# @app.post('/users')
# def create_user():
#     return {"Message":"User created successfully"}

# @app.put('/users/{user_id}')
# def update_user(user_id: int):
#     return {"Message":f"User with id {user_id} updated successfully"}

# @app.delete('/users/{user_id}')
# def delete_user(user_id: int):
#     return {"Message":f"User with id {user_id} deleted successfully"}


# @app.get('/products')
# def get_products():
#     return ['mobile','laptop']

# @app.get('/products/{product_id}')
# def get_product(product_id: int):
#     return {"Message":f"Product with id {product_id} details"}


# @app.get('/users')
# def get_users(age:int=0):
#     return {"age_filer":age}           Lesson 3


# @app.get('/items')
# def get_items(name:str="",price:int=0):
#     return {'name':name,'price':price}


# @app.get('/search')
# def search(q:str='',limit:int=10):
#     return {"query":q,"limit":limit}

# @app.post('/create_user')
# def create_user(user:User):
#     return {'user':user}


# @app.post("/user")
# def create_user(user:User):
#     users.append(user)
#     return {"message":"User added","data":user}

# @app.get("/users")
# def get_users():
#     return users

# @app.get("/users/{user_id}")
# def get_user(user_id:int):
#     for user in users:
#         if user.id==user_id:
#             return user
#     return{"error":"User not found"}


# @app.put("/users/{user_id}")
# def update_user(user_id:int, updated_user:User):
#     for i,user in enumerate(users):
#         if user.id==user_id:
#             users[i]=updated_user
#             return{"message":"User updated"}
#     return {"error":"User not found"}

# @app.delete("/users/{user_id}")
# def delete_user(user_id:int):
#     for i,user in enumerate(users):
#         if user.id==user_id:
#             users.pop(i)
#             return{"message":"User deleted"}
#     return {"error":"User not found"}


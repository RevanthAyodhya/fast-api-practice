from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

class User(BaseModel):
    name:str
    age:int
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


@app.get('/users')
def get_users(age:int=0):
    return {"age_filer":age}


@app.get('/items')
def get_items(name:str="",price:int=0):
    return {'name':name,'price':price}


@app.get('/search')
def search(q:str='',limit:int=10):
    return {"query":q,"limit":limit}

@app.post('/create_user')
def create_user(user:User):
    return {'user':user}

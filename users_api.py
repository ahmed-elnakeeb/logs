from fastapi import FastAPI,Query,Path
from manager import *
app=FastAPI()

@app.get("/")
def home():
    users=get_all_users()
    logs=get_all_logs()
    return {"users":users,"logs":logs}

@app.get("/user/{user_id}")
def get_user(user_id:int):
        users=get_all_users()
        
        for user in users:
            if user[0]==user_id:
                return{"user":user}
        return {"response":"notfound"}

@app.post("/new_user")
def new_user(user_name:str,user_password:str,user_email:str,user_phone:str):
    add_user(name=user_name,password=user_password,email=user_email,phone=user_phone)

    

from db import db

def get_all_users()->list:
    qry="select * from users"
    db1=db("./db_users_logs.db")
    db1.start_connection()
    users=db1.rows(qry)
    db1.stop_connection()
    return(users)

def get_all_logs()->list:
    qry="select * from logs"
    db1=db("./db_users_logs.db")
    db1.start_connection()
    logs=db1.rows(qry)
    db1.stop_connection()
    return(logs)

def add_user(name,password,email,phone=""):
    qry=f"insert into users(user_name,user_password,user_email,user_phone) values ('{name}','{password}','{email}','{phone}')"
    db1=db("./db_users_logs.db")
    db1.start_connection()
    db1.qurey(qry)
    db1.stop_connection()

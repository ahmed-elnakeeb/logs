import requests
import json

def post_user(user_name,user_password,user_email,user_phone=None,user_recovery_email=None):
    url = f'http://127.0.0.1:8000/new_user?user_name={user_name}&user_password={user_password}&user_email={user_email}'
    if (user_phone!=None):
        url=url+f"&user_phone={user_phone}"
    if (user_recovery_email!=None):
        url=url+f"&user_recovery_email={user_recovery_email}"
    x = requests.post(url)
    return(x.text)

print(post_user("ahmed55g","passs","ahmedeeeeee@lkj.dsdg","012745874"))
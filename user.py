class user:
    def __init__(self) -> None:
        pass
    
    def fromlist(self,user:list):
        self.user_id=user[0]
        self.user_name=user[1]
        self.user_password=user[2]
        self.user_email=user[3]
        self.user_phone=user[4]
        self.user_revovery_email=user[5]

    def todict(self):
        return {
        "user_id":self.user_id,
        "user_name":self.user_name,
        "user_password":self.user_password,
        "user_email":self.user_email,
        "user_phone":self.user_phone,
        "user_revovery_email":self.user_revovery_email,
        }


        
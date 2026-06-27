import uuid
from datetime import datetime


class User :
    def __init__(self, name, email, phone):
        self.__user_id = str(uuid.uuid4())
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__created_date = datetime.now()
        self.__accounts = []

    @property
    def user_id(self):
        return self.__user_id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def email(self):
        return self.__email
    
    @property
    def phone(self):
        return self.__phone
    
    @property
    def created_date(self):
        return self.__created_date
    
    @property
    def accounts(self):
        return tuple(self.__accounts)
    
    def change_email(self, email):
        if "@" not in email:
            raise ValueError("Invalid email")
        self.__email = email

    def change_phone(self, new_phone):
        if not new_phone.isdigit() or len(new_phone) != 10 :
            raise ValueError("Invalid phone")
        self.__phone = new_phone

    def _add_account(self, account):
        self.__accounts.append(account)
import uuid
from datetime import datetime
from uuid import UUID

from models.account import Account

class User :
    def __init__(self, name:str, email:str , phone:str , accounts = None, user_id:str = None, created_date:datetime = None ):
        self.__user_id = user_id or str(uuid.uuid4())
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__created_date = created_date or datetime.now()
        self.__accounts = accounts or []

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

    def to_dict(self):
        created_date = self.created_date.isoformat()

        accounts = []
        for account in self.accounts:
            accounts.append(account.account_number)

        return {
            "created_date" : created_date,
            "user_id":self.user_id,
            "name":self.name,
            "email":self.email,
            "phone":self.phone,
            "accounts":accounts
        }
    @classmethod
    def from_dict(cls, data):
        created_date = datetime.fromisoformat(data["created_date"])
        return cls(
            created_date = created_date,
            name = data["name"],
            email = data["email"],
            phone = data["phone"],
            user_id = data["user_id"],
            accounts = []


        )
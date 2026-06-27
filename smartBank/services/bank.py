
from models.user import User
from models.account import Account
from utils.enums import AccountType, AccountStatus

class Bank :
    def __init__(self):
        self.__users = {}
        self.__accounts = {}
        self.__emails = {}
        self.__phones = {}

    @property
    def users(self):
        return dict(self.__users)
    
    @property
    def accounts(self):
        return dict(self.__accounts)
    
    @property
    def emails(self):
        return dict(self.__emails)
    
    @property
    def phone(self):
        return dict(self.__phones)
    
    def register_user(self, name, email, phone):
        if email in self.__emails:
            raise ValueError("Email exists Already")
        
        if phone in self.__phones:
            raise ValueError("Phone Number already exists")
        
        user = User(name, email, phone)

        self.__users[user.user_id] = user
        self.__emails[user.email] = user.user_id
        self.__phones[user.phone] = user.user_id

        return user
    
    def find_user(self, user_id):
        if user_id is None:
            raise ValueError("User Id not Found")
        if  user_id not in self.__users:
            raise ValueError("User Does not exists")
        
        return self.__users[user_id]

    def find_account(self, account_number):
        if account_number is None:
            raise ValueError("Account Number not Found")
        if  account_number not in self.__accounts:
            raise ValueError("Account Does not exists")
        
        return self.__accounts[account_number]

    def open_account(self, user_id, account_type):
        # if user_id not in self.__users :
        #     raise ValueError("User does not exists")
        
        user = self.find_user(user_id)

        for account in user.accounts :
            if account.account_type == account_type :
                raise ValueError(f"User already has a {account_type.value} account.")
            
        account = Account(
            owner= user,
            account_type= account_type
        )
        self.__accounts[account.account_number] = account
        user._add_account(account)
        return account
    
    def deposit(self, account_number, amount,description = ""):
        account = self.find_account(account_number)

        if account.status != AccountStatus.ACTIVE:
            raise ValueError("Only active accounts can receive deposits.")
        return account._deposit(
            amount,
            description
        )
    
    def withdraw(self, account_number, amount,description = ""):
        account = self.find_account(account_number)

        if account.status != AccountStatus.ACTIVE:
            raise ValueError("Only active accounts can receive deposits.")
        return account._withdraw(
            amount,
            description
        )
    
    def transfer(self,sender_account_number,destination_account,amount,description = ''):
        account1 = self.find_account(sender_account_number)
        account2 = self.find_account(destination_account)

        if account1.status != AccountStatus.ACTIVE:
            raise ValueError("Only active accounts can receive deposits.")
        
        if account2.status != AccountStatus.ACTIVE:
            raise ValueError("Only active accounts can receive deposits.")
        return account1._transfer(amount, account2, description)
   
import uuid
from datetime import datetime
from utils.enums import TransactionStatus, TransactionType


class Transaction:
    def __init__(self, amount:float, balance_before:int, balance_after:int, transaction_type:TransactionType, receiver_account:str = None, description:str = ""):
        self.__transaction_id = uuid.uuid4()
        self.__timestamp= datetime.now()
        self.__status = TransactionStatus.PENDING
        self.__amount = amount
        self.__balance_before = balance_before
        self.__balance_after = balance_after
        self.__transaction_type = transaction_type
        self.__receiver_account = receiver_account
        self.__description = description
    
    @property
    def description(self):
        return self.__description
    @property
    def receiver_account(self):
        return self.__receiver_account
    @property
    def transaction_type(self):
        return self.__transaction_type
    @property
    def transaction_id(self):
        return self.__transaction_id
    @property
    def amount(self):
        return self.__amount
    @property
    def timestamp(self):
        return self.__timestamp
    @property
    def status(self):
        return self.__status
    
    
    def mark_success(self):
        self.__status = TransactionStatus.SUCCESS
    
    
    def mark_failed(self):
        self.__status = TransactionStatus.FAILED
    
    @property
    def balance_before(self):
        return self.__balance_before
    @property
    def balance_after(self):
        return self.__balance_after
    
    def __str__(self):
        result = (
            "Transaction Record\n"
            f"Transaction ID   : {self.transaction_id}\n"
            f"Timestamp        : {self.timestamp.strftime('%Y-%m-%d %H:%M:%S') }\n"
            f"Status           : {self.status}\n"
            f"Amount           : {self.amount}\n"
            f"Balance Before   : {self.balance_before}\n"
            f"Balance After    : {self.balance_after}\n"
            f"Transaction Type : {self.transaction_type}\n"
            
        )
        if self.description :
            result += f"Description      : {self.description}"
        if self.receiver_account:
            result += f"Receiver Account : {self.receiver_account}\n"
        return result
    

trans = Transaction(500, "Deposit", "Salary" )
print(trans)
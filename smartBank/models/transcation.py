from uuid import UUID
from datetime import datetime
import uuid
from utils.enums import TransactionStatus, TransactionType


class Transaction:
    def __init__(self, amount:float, balance_before:int, balance_after:int, transaction_type:TransactionType, related_account:str = None, description:str = "", transaction_id:uuid = None, timestamp:datetime = None, status:TransactionStatus = None):
        self.__transaction_id = transaction_id or uuid.uuid4()
        self.__timestamp= timestamp or datetime.now()
        self.__status = status or TransactionStatus.PENDING
        self.__amount = amount
        self.__balance_before = balance_before
        self.__balance_after = balance_after
        self.__transaction_type = transaction_type
        self.__related_account = related_account
        self.__description = description
    
    @property
    def description(self):
        return self.__description
    @property
    def related_account(self):
        return self.__related_account
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
            f"Status           : {self.status.value}\n"
            f"Amount           : {self.amount}\n"
            f"Balance Before   : {self.balance_before}\n"
            f"Balance After    : {self.balance_after}\n"
            f"Transaction Type : {self.transaction_type.value}\n"
            
        )
        if self.description :
            result += f"Description      : {self.description}"
        if self.related_account:
            result += f"Receiver Account : {self.related_account}\n"
        return result
    
    def to_dict(self):
        
        transaction_id = str(self.transaction_id)
        timestamp = self.timestamp.isoformat()
        transcation_type = self.transaction_type.value
        status = self.status.value

        return {
            "transaction_id": transaction_id,
            "status":status,
            "timestamp":timestamp,
            "transaction_type":transcation_type,
            "amount":self.amount,
            "balance_before":self.balance_before,
            "balance_after":self.balance_after,
            "related_account": self.related_account,
            "description": self.description
        }
    
    @classmethod
    def from_dict(cls, data):
        transaction_id = UUID(data["transaction_id"])
        timestamp = datetime.fromisoformat(data["timestamp"])
        status = TransactionStatus(data["status"])
        transaction_type = TransactionType(data["transaction_type"])

        return cls(
            transaction_id = transaction_id, 
            timestamp = timestamp, 
            status = status, 
            transaction_type = transaction_type, 
            amount = data["amount"], 
            balance_before = data["balance_before"],
            balance_after = data["balance_after"],
            related_account = data["related_account"],
            description = data["description"]
        )


    


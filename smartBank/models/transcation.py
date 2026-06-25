import uuid
from datetime import datetime


class Transaction:
    def __init__(self, amount:float, transaction_type:str, description:str = ""):
        self.transaction_id = uuid.uuid4()
        self.timestamp= datetime.now()
        self.status = "Pending"
        self.amount = amount
        self.transaction_type = transaction_type
        self.description = description
    
    def __str__(self):
        result = (
            "Transaction Record\n"
            f"Transaction ID   : {self.transaction_id}\n"
            f"Timestamp        : {self.timestamp.strftime("%Y-%m-%d %H:%M:%S") }\n"
            f"Status           : {self.status}\n"
            f"Amount           : {self.amount}\n"
            f"Transaction Type : {self.transaction_type}\n"
            
        )
        if self.description :
            result += f"Description      : {self.description}"
        
        return result
    

trans = Transaction(500, "Deposit", "Salary" )
print(trans)
import uuid
from datetime import datetime
from models.transcation import Transaction
from utils.enums import AccountStatus, TransactionType, TransactionStatus
def generate_account_number():
    return str(uuid.uuid4())


class Account:
    def __init__(self,owner, account_type):
        self.__balance = 0
        self.__account_number = generate_account_number()
        self.__created_date = datetime.now()
        self.__owner = owner
        self.__account_type = account_type
        self.__status = AccountStatus.ACTIVE
        self.__transactions = []
        self.__currency = "NPR"

    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def balance(self):
        return self.__balance
    
    @property
    def created_date(self):
        return self.__created_date
    
    @property
    def owner(self):
        return self.__owner
    
    @property
    def account_type(self):
        return self.__account_type
    
    @property
    def status(self):
        return self.__status
    
    
    @property
    def currency(self):
        return self.__currency
    
    @property
    def transactions(self):
        return tuple(self.__transactions)
    
    def _deposit (self, amount, description = ''):
        if amount <= 0 : 
            raise ValueError("Amount must be Positive")
        
        balance_before = self.balance
        self.__balance += amount
        balance_after = self.balance

        transaction = Transaction(
            amount=amount,
            balance_before=balance_before,
            balance_after=balance_after,
            transaction_type=TransactionType.DEPOSIT,
            description=description
        )
        transaction.mark_success()
        self.__transactions.append(transaction)
        return transaction
    
    def _withdraw (self, amount, description = ''):
        if amount <= 0 : 
            raise ValueError("Amount must be Positive")
        
        if self.balance < amount :
            raise ValueError("Balance Not Enough")
        
        balance_before = self.balance
        self.__balance -= amount
        balance_after = self.balance

        transaction = Transaction(
            amount=amount,
            balance_before=balance_before,
            balance_after=balance_after,
            transaction_type=TransactionType.WITHDRAW,
            description=description
        )
        transaction.mark_success()
        self.__transactions.append(transaction)
        return transaction

    def _transfer(self, amount,destination_account, description = ''):
        
        if destination_account is None:
                raise ValueError("Destination Account is required")
        
        if destination_account == self :
            raise ValueError("Cannot be transferred to self")
            
        if amount <= 0:
            raise ValueError("Amount must be positive")
            
        if self.balance < amount :
            raise ValueError("Amount not Enough")
            
        sender_before = self.balance
        receiver_before = destination_account.balance


        try:
            
            self.__balance -= amount
            destination_account.__balance += amount

            sender_transaction = Transaction(
                amount=amount,
                balance_before=sender_before,
                balance_after=self.__balance,
                transaction_type=TransactionType.WITHDRAW,
                related_account=destination_account.account_number,
                description=description
            )

            receiver_transaction = Transaction(
                amount=amount,
                balance_before=receiver_before,
                balance_after=destination_account.__balance,
                transaction_type=TransactionType.DEPOSIT,
                related_account=self.account_number,
                description=description
            )

            sender_transaction.mark_success()
            receiver_transaction.mark_success()

            self.__transactions.append(sender_transaction)

            destination_account.__transactions.append(
                receiver_transaction
            )

            return (
                sender_transaction,
                receiver_transaction
            )

        except Exception :

            self.__balance = sender_before
            destination_account.__balance = receiver_before

            raise
        
        


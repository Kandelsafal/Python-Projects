from models.account import Account
from utils.enums import AccountType

account1 = Account("Safal", AccountType.SAVINGS)
account2 = Account("Kandel", AccountType.SAVINGS)
account1.deposit(
    amount=1000,
    description="Initial dep"
)
account2.deposit(
    amount=1000,
    description="Initial dep"
)

sender_trans, reciever_trans = account1.transfer(
    amount=300,
    destination_account= account2
    
)
print("ACCOUNT NUMBER SENDER:", account1.account_number)
print("ACCOUNT NUMBER Reciever", account2.account_number)
print("Balance_)Sender:", account1.balance)
print("Balance_)Reciever:", account2.balance)
print("Transaction Record", sender_trans, reciever_trans)
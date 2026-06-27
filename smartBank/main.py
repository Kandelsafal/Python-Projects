from models.account import Account
from services.bank import Bank
from utils.enums import AccountType

bank = Bank()

user = bank.register_user(
    "SafalKandel",
    "safal@gmail.com",
    "9800000000"
)

account1 = bank.open_account(
    user.user_id,
    AccountType.SAVINGS
)

print("First account created:", account1.account_number)

account2 = bank.open_account(
    user.user_id,
    AccountType.CURRENT
)

print("Second account created:", account2.account_number)

bank.open_account(
    user.user_id,
    AccountType.SAVINGS
)
# user1 = bank.register_user("Alice", "alice@gmail.com", "9800000001")

# print("User 1 created:", user1.user_id)

# user2 = bank.register_user("Bob", "alices@gmail.com", "9800000001")

# print("User 2 created:", user2.name)

# account1 = Account("Safal", AccountType.SAVINGS)
# account2 = Account("Kandel", AccountType.SAVINGS)
# account1.deposit(
#     amount=1000,
#     description="Initial dep"
# )
# account2.deposit(
#     amount=1000,
#     description="Initial dep"
# )

# sender_trans, reciever_trans = account1.transfer(
#     amount=300,
#     destination_account= account2
    
# )
# print("ACCOUNT NUMBER SENDER:", account1.account_number)
# print("ACCOUNT NUMBER Reciever", account2.account_number)
# print("Balance_)Sender:", account1.balance)
# print("Balance_)Reciever:", account2.balance)
# print("Transaction Record", sender_trans, reciever_trans)
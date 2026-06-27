from services.bank import Bank
from utils.enums import AccountType

bank = Bank()

# Register users
user1 = bank.register_user(
    "Safal",
    "safal@gmail.com",
    "9800000000"
)

user2 = bank.register_user(
    "Alice",
    "alice@gmail.com",
    "9800000001"
)

# Open accounts
account1 = bank.open_account(
    user1.user_id,
    AccountType.SAVINGS
)

account2 = bank.open_account(
    user2.user_id,
    AccountType.CURRENT
)

# Perform some transactions
bank.deposit(
    account1.account_number,
    1000,
    "Initial Deposit"
)

bank.transfer(
    account1.account_number,
    account2.account_number,
    300,
    "Transfer to Alice"
)

# Serialize the whole bank
bank_data = bank.to_dict()

bank.save("bank.json")
print("Bank Saved sucessfully")
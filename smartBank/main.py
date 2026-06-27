from services.bank import Bank
from models.account import Account
from utils.enums import AccountType, TransactionType

bank = Bank()


# # Register a user
user = bank.register_user(
    "Safal",
    "safal@gmail.com",
    "9800000000"
)

# Open an account through the Bank
account = bank.open_account(
    user.user_id,
    AccountType.SAVINGS
)
bank.deposit(
    account.account_number,
    1000,
    "Initial"
)
# ----------------------------
# Convert to dictionary
# ----------------------------
account_data = account.to_dict()

print("Serialized Account")
print(account_data)

# Prepare users dictionary
# ----------------------------
users = {
    user.user_id: user
}

# Restore Account
# ----------------------------
restored_account = Account.from_dict(
    account_data,
    users
)

print("\nRestored Account")

print("Account Number :", restored_account.account_number)
print("Owner          :", restored_account.owner.name)
print("Balance        :", restored_account.balance)
print("Status         :", restored_account.status)
print("Account Type   :", restored_account.account_type)
print("Transactions   :", len(restored_account.transactions))
# # Deposit through the Bank
# transaction = bank.deposit(
#     account1.account_number,
#     amount=1000,
#     description="Initial Deposit"
# )

# account1_rec, account2_rec = bank.transfer(
#     account1.account_number,
#     account2.account_number,
#     amount=100,
#     description="Initial Deposit"
# )


# print("Transfer Successful")
# print("Balance:", account2.balance)
# print(account1_rec)
# print(account2_rec)
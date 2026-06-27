from services.bank import Bank
from models.account import Account
from models.user import User
from utils.enums import AccountType, TransactionType

bank = Bank()


# # Register a user
user = bank.register_user(
    "Safal",
    "safal@gmail.com",
    "9800000000"
)
# Convert to dictionary
user_data = user.to_dict()

print("Dictionary:")
print(user_data)

# Convert back to User object
new_user = User.from_dict(user_data)

print("\nRestored User")
print("ID:", new_user.user_id)
print("Name:", new_user.name)
print("Email:", new_user.email)
print("Phone:", new_user.phone)
print("Created:", new_user.created_date)
print("Accounts:", new_user.accounts)

# # Open an account through the Bank
# account = bank.open_account(
#     user.user_id,
#     AccountType.SAVINGS
# )
# bank.deposit(
#     account.account_number,
#     1000,
#     "Initial"
# )
# # ----------------------------
# # Convert to dictionary
# # ----------------------------
# account_data = account.to_dict()

# print("Serialized Account")
# print(account_data)

# # Prepare users dictionary
# # ----------------------------
# users = {
#     user.user_id: user
# }

# # Restore Account
# # ----------------------------
# restored_account = Account.from_dict(
#     account_data,
#     users
# )

# print("\nRestored Account")

# print("Account Number :", restored_account.account_number)
# print("Owner          :", restored_account.owner.name)
# print("Balance        :", restored_account.balance)
# print("Status         :", restored_account.status)
# print("Account Type   :", restored_account.account_type)
# print("Transactions   :", len(restored_account.transactions))
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
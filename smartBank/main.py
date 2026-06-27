from services.bank import Bank
from utils.enums import AccountType

bank = Bank()


from models.transcation import Transaction
from utils.enums import TransactionType

# Create an original transaction
transaction = Transaction(
    amount=1000,
    balance_before=0,
    balance_after=1000,
    transaction_type=TransactionType.DEPOSIT,
    description="Initial Deposit"
)

print("========== ORIGINAL TRANSACTION ==========")
print(transaction)

# Convert object -> dictionary
transaction_data = transaction.to_dict()

print("\n========== DICTIONARY ==========")
print(transaction_data)

# Convert dictionary -> object
loaded_transaction = Transaction.from_dict(transaction_data)

print("\n========== LOADED TRANSACTION ==========")
print(loaded_transaction)

print("\n========== FIELD COMPARISON ==========")

print(transaction.to_dict() == loaded_transaction.to_dict())

# # Register a user
# user1 = bank.register_user(
#     "Safal",
#     "safal@gmail.com",
#     "9800000000"
# )

# user2 = bank.register_user(
#     "Safal",
#     "safaal@gmail.com",
#     "9800200000"
# )
# # Open an account through the Bank
# account1 = bank.open_account(
#     user1.user_id,
#     AccountType.SAVINGS
# )
# account2 = bank.open_account(
#     user2.user_id,
#     AccountType.SAVINGS
# )

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
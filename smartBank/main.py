from services.bank import Bank
from utils.enums import AccountType

print("=" * 60)
print("CREATING BANK")
print("=" * 60)

bank = Bank()

# Create users
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

# Transactions
bank.deposit(
    account1.account_number,
    1000,
    "Initial Deposit"
)

bank.withdraw(
    account1.account_number,
    100,
    "ATM Withdrawal"
)

bank.transfer(
    account1.account_number,
    account2.account_number,
    300,
    "Transfer to Alice"
)

print("\nSaving bank...")
bank.save("bank.json")
print("Bank saved successfully!")

# Simulate closing the application
del bank

print("\n" + "=" * 60)
print("LOADING BANK")
print("=" * 60)

loaded_bank = Bank.load("bank.json")

print("\nBank loaded successfully!")
loaded_bank.register_user(
    "Safal",
    "safal@gmail.com",
    "9800000000"
)
print("\nUsers Loaded:", len(loaded_bank._Bank__users))
print("Accounts Loaded:", len(loaded_bank._Bank__accounts))

print("\n" + "=" * 60)
print("BANK DATA")
print("=" * 60)

for user in loaded_bank._Bank__users.values():

    print(f"\nUser: {user.name}")
    print(f"User ID : {user.user_id}")
    print(f"Email   : {user.email}")
    print(f"Phone   : {user.phone}")

    print(f"\nAccounts ({len(user.accounts)}):")

    for account in user.accounts:

        print("-" * 40)
        print("Account Number :", account.account_number)
        print("Account Type   :", account.account_type.value)
        print("Balance        :", account.balance)
        print("Status         :", account.status.value)

        print("\nTransactions:")

        for transaction in account.transactions:

            print(
                f"  {transaction.transaction_type.value:10}"
                f" Amount: {transaction.amount:<8}"
                f" Balance: {transaction.balance_after:<8}"
                f" Status: {transaction.status.value}"
            )

print("\n" + "=" * 60)
print("LOAD TEST PASSED")
print("=" * 60)
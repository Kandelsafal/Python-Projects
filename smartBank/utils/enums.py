from enum import Enum

class AccountStatus(Enum):
    ACTIVE = "Active"
    FROZEN = "Frozen"
    CLOSED = "Closed"

class TransactionType(Enum):
    DEPOSIT = "Deposit"
    WITHDRAW = "Withdraw"
    TRANSFER = "Transfer"

class TransactionStatus(Enum):
    PENDING = "Pending"
    SUCCESS = "Success"
    FAILED = "Failed"

class AccountType(Enum):
    SAVINGS = "Savings"
    CURRENT = "Current"
    FIXED_DEPOSIT = "Fixed Deposit"


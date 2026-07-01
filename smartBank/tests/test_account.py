from models.account import Account
from utils.enums import AccountType
import pytest
from models.user import User

name = "ram"
email = "ram@gmail.com"
phone = "9800000000"
user = User(name, email, phone)

account_type = AccountType.SAVINGS
account = Account(user, account_type)
def test_account_is_created_with_correct_details():
    name = "ram"
    email = "ram@gmail.com"
    phone = "9800000000"
    user = User(name, email, phone)

    account_type = AccountType.SAVINGS
    account = Account(user, account_type)
    assert account.owner == user
    assert account.account_type == account_type
    assert account.balance == 0
    assert account.transactions == ()

def test_deposit_increases_balance():
    
    account._deposit(2000, 'salary')
    assert account.balance == 2000
    assert len(account.transactions) > 0

def test_deposit_raises_value_error_for_negative_amount():

    with pytest.raises(ValueError):
        account._deposit(-200)
    assert account.balance == 2000
    assert len(account.transactions) == 1

def test_withdraw_decreases_balance():
    
    account._withdraw(1000, 'salary')
    assert account.balance == 1000
    assert len(account.transactions) > 1

def test_withdraw_raises_value_error_for_insufficient_balance():

    with pytest.raises(ValueError):
        account._withdraw(3000)
        
def test_transaction_is_added_after_successful_deposit():

    account._deposit(1000)
    assert len (account.transactions) > 0
    
def test_account_serializes_correctly():
    
    assert set(account.to_dict().keys()) == {
         "owner_id" ,
            "status" ,
            "account_type",
            "balance",
            "account_number",
            'currency',
            "created_date",
            "transactions",
    }
    assert isinstance(account.to_dict(), dict)
def test_account_deserialization_correctly():

    oldAccount = account.to_dict()
    users = {
    user.user_id: user
    }
    newAccount = Account.from_dict(oldAccount, users)

    assert newAccount.owner == account.owner
    assert newAccount.status == account.status
    assert newAccount.account_number == account.account_number
    assert newAccount.account_type == account.account_type
    assert newAccount.balance == account.balance
    assert newAccount.currency == account.currency
    assert newAccount.created_date == account.created_date
    assert len(newAccount.transactions) == len(account.transactions)
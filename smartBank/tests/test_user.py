from models.user import User
from datetime import datetime
import pytest
name = "ram"
email = "ram@gmail.com"
phone = "9800000000"
def test_user_is_created_with_correct_details():
    user = User(
        name, email, phone
    )

    assert user.name == name
    assert user.email == email
    assert user.phone == phone

def test_new_user_starts_with_no_accounts():
    user = User(
        name, email, phone
    )

    assert user.accounts == ()

def test_new_user_has_generated_user_id():
    user = User (name, email, phone)

    assert user.user_id is not None
    assert isinstance(user.user_id, str)
    assert len(user.user_id) > 0

def test_new_user_has_created_date():
    user = User(name, email, phone)

    assert user.created_date is not None
    assert isinstance(user.created_date, datetime)

def test_change_email_updates(updatedEmail = 'shyam@gmaill.com'):
    user = User(name, email, phone)

    assert user.email == email
    print("Old email passed")
    user.change_email(updatedEmail)
    assert user.email == updatedEmail
    print("New Email Passed")

def test_change_email_raises_value_error_for_invalid_email():
    user = User (name, email, phone)

    with pytest.raises(ValueError):
        user.change_email("ramgmail.com")
    
def test_change_phone_updates(updatedphone = '9898765432'):
    user = User(name, email, phone)

    assert user.phone == phone
    
    user.change_phone(updatedphone)
    assert user.phone == updatedphone
    

def test_change_phone_raises_value_error_for_invalid_phone():
    user = User (name, email, phone)

    with pytest.raises(ValueError):
        user.change_phone('123')
    

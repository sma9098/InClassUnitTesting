import pytest
from bank_account.bank_account import BankAccount


@pytest.fixture
def start_account():
    return BankAccount(100)

# def test_deposit(start_account):
#     start_account.deposit(50)
#     assert start_account.balance == 150

# balance test
def test_init_negative_balance():
    with pytest.raises(ValueError):
        BankAccount(-10)

def test_init_valid_balance():
    acc = BankAccount(50)
    assert acc.balance == 50

#deposit test
def test_deposit(start_account):
    start_account.deposit(50)
    assert start_account.balance == 150

def test_deposit_invalid_amount(start_account):
    with pytest.raises(ValueError):
        start_account.deposit(0)

    with pytest.raises(ValueError):
        start_account.deposit(-10)

# withdraw test
def test_withdraw_success(start_account):
    start_account.withdraw(40)
    assert start_account.balance == 60


def test_withdraw_invalid_amount(start_account):
    with pytest.raises(ValueError):
        start_account.withdraw(0)

    with pytest.raises(ValueError):
        start_account.withdraw(-5)

def test_withdraw_insufficient_funds(start_account):
    with pytest.raises(ValueError):
        start_account.withdraw(200)

# transfer test
def test_transfer_success():
    acc1 = BankAccount(100)
    acc2 = BankAccount(50)

    acc1.transfer_to(acc2, 30)

    assert acc1.balance == 70
    assert acc2.balance == 80

def test_transfer_invalid_target(start_account):
    with pytest.raises(ValueError):
        start_account.transfer_to("not_account", 10)

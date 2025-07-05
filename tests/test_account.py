import sys, pathlib; sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
import pytest
from Account import Account


def test_deposit_positive_increases_balance():
    acct = Account(1, 100)
    acct.deposit(50)
    assert acct.get_balance() == 150


def test_deposit_negative_does_not_change_balance():
    acct = Account(1, 100)
    acct.deposit(-20)
    assert acct.get_balance() == 100


def test_withdraw_more_than_balance_fails_and_unchanged():
    acct = Account(1, 100)
    result = acct.withdraw(150)
    assert result is False
    assert acct.get_balance() == 100


def test_valid_withdraw_decreases_balance():
    acct = Account(1, 100)
    result = acct.withdraw(40)
    assert result is True
    assert acct.get_balance() == 60


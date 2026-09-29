from database import accounts
from transactions import withdraw


def test_withdraw():

    print("Testing withdrawal...")

    old_balance = accounts["1001"]["balance"]

    withdraw("1001")

    new_balance = accounts["1001"]["balance"]

    if new_balance < old_balance:
        print("Withdrawal test passed!")
    else:
        print("Withdrawal test failed!")


test_withdraw()
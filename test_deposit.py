from database import accounts
from transactions import deposit


def test_deposit():

    print("Testing deposit...")

    old_balance = accounts["1001"]["balance"]

    deposit("1001")

    new_balance = accounts["1001"]["balance"]

    if new_balance > old_balance:
        print("Deposit test passed!")
    else:
        print("Deposit test failed!")


test_deposit()
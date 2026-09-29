from database import accounts
from validation import validate_amount


def check_balance(account_number):
    balance = accounts[account_number]["balance"]
    print(f"\nAvailable Balance: ₹{balance:.2f}")


def deposit(account_number):
    amount_input = input("Enter amount to deposit: ₹")

    if not validate_amount(amount_input):
        print("Invalid amount.")
        return

    amount = float(amount_input)

    accounts[account_number]["balance"] += amount
    accounts[account_number]["transactions"].append(
        f"Deposited ₹{amount:.2f}"
    )

    print(f"₹{amount:.2f} deposited successfully.")


def withdraw(account_number):
    amount_input = input("Enter amount to withdraw: ₹")

    if not validate_amount(amount_input):
        print("Invalid amount.")
        return

    amount = float(amount_input)

    if amount > accounts[account_number]["balance"]:
        print("Insufficient balance.")
        return

    accounts[account_number]["balance"] -= amount
    accounts[account_number]["transactions"].append(
        f"Withdrawn ₹{amount:.2f}"
    )

    print(f"Please collect your cash: ₹{amount:.2f}")


def transfer(account_number):
    receiver = input("Enter receiver account number: ")

    if receiver not in accounts:
        print("Receiver account not found.")
        return

    amount_input = input("Enter amount to transfer: ₹")

    if not validate_amount(amount_input):
        print("Invalid amount.")
        return

    amount = float(amount_input)

    if amount > accounts[account_number]["balance"]:
        print("Insufficient balance.")
        return

    accounts[account_number]["balance"] -= amount
    accounts[receiver]["balance"] += amount

    accounts[account_number]["transactions"].append(
        f"Transferred ₹{amount:.2f} to {receiver}"
    )

    accounts[receiver]["transactions"].append(
        f"Received ₹{amount:.2f} from {account_number}"
    )

    print("Money transferred successfully.")
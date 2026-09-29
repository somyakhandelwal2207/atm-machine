from database import accounts


def login():
    account_number = input("Enter account number: ")
    pin = input("Enter PIN: ")

    if account_number in accounts:
        if accounts[account_number]["pin"] == pin:
            print("\nLogin successful!")
            print("Welcome,", accounts[account_number]["name"])
            return account_number

    print("\nInvalid account number or PIN.")
    return None
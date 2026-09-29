from database import accounts


def create_account():
    name = input("Enter your name: ")
    pin = input("Create PIN: ")
    balance = float(input("Enter initial deposit: "))

    account_number = str(1000 + len(accounts) + 1)

    accounts[account_number] = {
        "name": name,
        "pin": pin,
        "balance": balance,
        "transactions": []
    }

    print("\nAccount created successfully!")
    print("Your account number is:", account_number)


def get_account_details(account_number):
    account = accounts[account_number]

    print("\nName:", account["name"])
    print("Account Number:", account_number)
    print("Balance: ₹", account["balance"])


def change_pin(account_number):
    new_pin = input("Enter new PIN: ")
    accounts[account_number]["pin"] = new_pin
    print("PIN changed successfully!")
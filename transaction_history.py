from database import accounts


def add_transaction(account_number, transaction):
    accounts[account_number]["transactions"].append(transaction)


def show_history(account_number):
    print("\n========== TRANSACTION HISTORY ==========")

    history = accounts[account_number]["transactions"]

    if len(history) == 0:
        print("No transactions available.")
        return

    for number, transaction in enumerate(history, start=1):
        print(f"{number}. {transaction}")
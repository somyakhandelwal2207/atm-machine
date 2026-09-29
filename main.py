from authentication import login
from atm import atm_menu
from account import create_account


def main():

    while True:

        print("\n===== ATM MACHINE =====")
        print("1. Login")
        print("2. Create New Account")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = login()

            if account_number:
                atm_menu(account_number)

        elif choice == "2":
            create_account()

        elif choice == "3":
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
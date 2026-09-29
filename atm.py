from transactions import check_balance, deposit, withdraw, transfer
from account import get_account_details, change_pin
from transaction_history import show_history


def atm_menu(account_number):

    while True:

        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Account Details")
        print("6. Transaction History")
        print("7. Change PIN")
        print("8. Logout")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(account_number)

        elif choice == "2":
            deposit(account_number)

        elif choice == "3":
            withdraw(account_number)

        elif choice == "4":
            transfer(account_number)

        elif choice == "5":
            get_account_details(account_number)

        elif choice == "6":
            show_history(account_number)

        elif choice == "7":
            change_pin(account_number)

        elif choice == "8":
            print("\nThank you for using the ATM!")
            break

        else:
            print("Invalid choice. Please select 1-8.")
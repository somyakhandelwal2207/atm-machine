def validate_amount(amount):
    try:
        amount = float(amount)

        if amount <= 0:
            return False

        return True

    except ValueError:
        return False


def validate_pin(pin):
    return len(pin) == 4 and pin.isdigit()


def validate_account_number(account_number):
    return account_number.isdigit() and len(account_number) == 4
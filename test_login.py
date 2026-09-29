from authentication import login


def test_login():
    print("Testing login...")

    account = login()

    if account:
        print("Login test passed!")
    else:
        print("Login test failed!")


test_login()
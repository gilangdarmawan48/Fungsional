from getpass import getpass

from model.user import User

from utils.utils import message


# authentication
def login(accounts: dict):
    error_message = ""

    print("\nlogin Page")
    username = input('type username : ')
    password = getpass('type password : ')

    for account in accounts.values():
        if username == account.username:
            return account
        if username != account.username:
            error_message = "username tidak terdaftar"
        elif password != account.password:
            error_message = "password salah"

    if (not error_message):
        message(error_message)
        login(accounts)


def register(accounts: dict):
    print("\nRegister Page")
    username = input('type username : ')
    password = getpass('type password : ')

    for account in accounts.values():
        if username == account.username:
            message("account sudah terdaftar")
            register(accounts)

    return User(username, password)

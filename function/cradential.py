from getpass import getpass

from model.user import User

from utils.utils import message

# authentication


def login(accounts: dict):
    print("\nlogin Page")
    username = input('type username : ')
    password = getpass('type password : ')

    for account in accounts.values():
        if username != account.username:
            message("username tidak terdaftar")
            login(accounts)
        elif password != account.password:
            message("password salah")
            login(accounts)

    return account


def register(accounts: dict):
    print("\nRegister Page")
    username = input('type username : ')
    password = getpass('type password : ')

    for account in accounts.values():
        if username == account.username:
            message("account sudah terdaftar")
            register(accounts)

    return User(username, password)

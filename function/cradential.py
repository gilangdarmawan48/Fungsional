from getpass import getpass
import re

from model.user import User

from utils.utils import message


# authentication
def login(accounts: dict):
    error_message = ""

    print("\nlogin Page")
    username = input('type username : ')
    password = getpass('type password : ')

    for account in accounts.values():
        if username == account.username and password == account.password:
            return account

    if username != account.username:
        message("username tidak terdaftar")
        return login(accounts)
    if password != account.password:
        message("password salah")
        return login(accounts)

    return account


def register(accounts: dict):
    print("\nRegister Page")
    username = input('type username : ')
    password = getpass('type password : ')

    for account in accounts.values():
        if username == account.username:
            message("account sudah terdaftar")
            return register(accounts)

    return User(username, password)

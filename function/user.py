from getpass import getpass

from model.user import User

from utils.utils import message


# user management
def shows_user(accounts: dict):
    for key, account in accounts.items():
        print(' ', key, ' | ', account.username)


def create_user(accounts: dict):
    print("\nCreate User")
    username = input('type username : ')
    password = getpass('type password : ')

    for account in accounts.values():
        if username == account.username:
            message("account sudah tersedia")
            return create_user(accounts)

    return {len(accounts): User(username, password)}


def update_user(accounts: dict):
    update = False

    print("\nUpdate User")
    for key, account in accounts.items():
        print(' ', key, ' | ', account.username)

    if len(accounts) > 0:
        no_user = input('\npilih user : ')

        for key, account in accounts.items():
            if key == int(no_user):
                update = True

        if (update):
            username = input('type username : ')
            password = getpass('type password : ')

            accounts[int(no_user)] = User(
                username, password, role=account.role)

            print(" v | account berhasil di update")
        else:
            print(" e | account does not exist")
            return update_user(accounts)
    else:
        print(" e | accounts is empty")

    return accounts


def delete_user(accounts: dict, user: User):
    delete = False

    print("\nDelete User")
    for key, account in accounts.items():
        if account != user:
            print(' ', key, ' | ', account.username)
            delete = True

    if delete:
        no_user = input('\npilih user : ')
        delete = False

        for key, account in accounts.items():
            if key == int(no_user) and account != user:
                delete = True

        if account == user:
            print(" e | account canot deleted")
            return delete_user(accounts, user)

        if (delete):
            del accounts[int(no_user)]
            print(" v | account berhasil di delete")
        else:
            print(" e | account does not exist")
            return delete_user(accounts, user)
    else:
        print(" e | accounts is empty")

    return accounts

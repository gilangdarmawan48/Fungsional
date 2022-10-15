from getpass import getpass

from utils import constant as const
from utils.utils import message

from model.user import User

from function.book import input_book, borrow_book, return_book, shows_book

base_accounts = {0: const.USER_ADMIN}
base_books = {
    0: const.BOOKS[0],
    1: const.BOOKS[1],
    2: const.BOOKS[2],
    3: const.BOOKS[3],
}


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


def dashboard(user: User, books: dict, accounts: dict, books_temp={}):
    admin = user.role == const.ADMIN

    print("\nDashboard Page")
    print(' 1 | shows buku')
    print(' 2 | pinjam buku')

    if admin:
        print(' 3 | input buku')
        print(' 4 | delet buku')
        print(' 5 | updet buku')
        print(' 6 | kembalikan buku')
        print(' 7 | tampil user')
        print(' 8 | create user')
        print(' 9 | update user')
        print(' 10 | delete user')
        print(' 11 | logout')
    else:
        print(' 3 | kembalikan buku')
        print(' 4 | logout')

    menu = input("\npilih ")

    if menu == "1" and admin:
        shows_book(books)
        dashboard(user, books, accounts)

    elif menu == "2":
        if(len(books_temp) < 3):

            books_temp.update(borrow_book(user, books))
            print(books_temp)

            dashboard(user, books.update(books_temp), accounts)
        else:
            print(" e | peminjaman maksimal 3 \n")
            dashboard(user, books, accounts)

    elif menu == "3" and admin:
        books = input_book(user, books)
        dashboard(user, books, accounts)

    elif menu == "4" and admin:
        pass
    elif menu == "5" and admin:
        pass
    elif menu == "6" and admin:
        books = return_book(user, books)
        dashboard(user, books, accounts)

    elif menu == "7" and admin:
        pass
    elif menu == "8" and admin:
        pass
    elif menu == "9" and admin:
        pass
    elif menu == "10" and admin:
        pass
    elif menu == "11" and admin:
        home_page(accounts, books)

    elif menu == "3":
        books = return_book(user, books)

    elif menu == "4":
        home_page(accounts, books)

    else:
        print(" e | inputan salah \n")
        dashboard(user, books, accounts)


# home_page
def home_page(accounts=dict, books=dict):

    print("\nPeminjaman Buku")
    print(" 1 | login")
    print(" 2 | register")
    print(" 3 | exit")

    menu = input("\npilih ")

    if menu == "1":
        user = login(accounts)

        dashboard(user, books, accounts)
    elif menu == "2":
        user = register(accounts)
        indx = len(accounts)

        accounts[indx] = user

        dashboard(user, books, accounts)
    elif menu == "3":
        exit()
    else:
        print(" e | inputan salah \n")
        home_page(accounts)


# running
home_page(base_accounts, base_books)

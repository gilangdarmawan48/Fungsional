from getpass import getpass

from utils import constant as const
from utils import utils
from model.user import User
from model.book import Book

base_accounts = {0: const.USER_ADMIN}
base_books = {
    0: const.BOOKS[0],
    1: const.BOOKS[1],
    2: const.BOOKS[2],
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


# handling respon
def message(msg):
    print(str(msg))


# access library
def check_book(books: dict, case: str, param=any, value={}):
    # validate
    for key, book in books.items():
        if case == const.BORROW_BOOK:
            if book.borrower == User:
                print(' ', key, ' | ', book.title)
                value[key] = book

        if case == const.INPUT_BOOK:
            if str(param) == book.title:
                return True

        if case == const.RETURN_BOOK:
            if book.borrower == param:
                print(' ', key, ' | ', book.title)
                value[key] = book

    if case == const.BORROW_BOOK:
        return value
    if case == const.RETURN_BOOK:
        return value


def borrow_book(user: User, books: dict, accounts: dict):
    print("\nPinjam Buku")
    books_can_borrow = check_book(books, const.BORROW_BOOK)

    pinjam_buku = input('\npilih buku : ')

    for key, book in books_can_borrow.items():
        if pinjam_buku == book.title or pinjam_buku == str(key):
            books[key] = Book(book.title, user)
            print(' v | buku berhasil di pinjam')
            dashboard(user, books, accounts)

    print(' e | buku tidak dapat dipinjam')
    borrow_book(user, books, accounts)


def return_book(user: User, books: dict, accounts: dict):
    print("\nKembalikan Buku")
    books_can_return = check_book(books, const.RETURN_BOOK, user)

    if books_can_return:
        book_title = input('\npilih buku : ')

        for key, book in books_can_return.items():
            if return_book == book.title or book_title == str(key):
                books[key] = Book(book.title)
                print(' v | buku berhasil di kembalikan')
                dashboard(user, books, accounts)
    else:
        print(' e | empty borrowed books')
        dashboard(user, books, accounts)

    print(' e | book not exist')
    return_book(user, books, accounts)


def input_book(user: User, books: dict,  accounts: dict):
    print("\nInput Buku")
    book_title = input('judul buku : ')
    already_exist = bool(check_book(books, const.INPUT_BOOK, book_title))

    if not already_exist:
        books[len(books)] = Book(book_title.title())
        print(" v | buku berhasil di inputkan")
    else:
        print(" e | book already exist")
        input_book(user, books, accounts)

    dashboard(user, books, accounts)


def dashboard(user: User, books: dict, accounts: dict):
    print(user)
    admin = user.role == const.ADMIN

    print("\nDashboard Page")
    print(' 1 | pinjam buku')

    if admin:
        print(' 2 | input buku')
        print(' 3 | kembalikan buku')
        print(' 4 | logout')
    else:
        print(' 2 | kembalikan buku')
        print(' 3 | logout')

    menu = input("\npilih ")

    if menu == "1":
        borrow_book(user, books, accounts)
    elif menu == "2" and admin:
        input_book(user, books, accounts)
    elif menu == "3" and admin:
        return_book(user, books, accounts)
    elif menu == "4" and admin:
        home_page(accounts, books)
    elif menu == "2":
        return_book(user, books, accounts)
    elif menu == "3":
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

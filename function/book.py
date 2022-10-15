from utils import constant as const
from model.user import User
from model.book import Book


# access library
def shows_book(books: dict):
    for key, book in books.items():
        print(' ', key, ' | ', book.title)

    return


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


def borrow_book(user: User, books: dict):
    print("\nPinjam Buku")
    books_can_borrow = check_book(books, const.BORROW_BOOK)

    pinjam_buku = input('\npilih buku : ')

    for key, book in books_can_borrow.items():
        if pinjam_buku == book.title or pinjam_buku == str(key):
            books[key] = Book(book.title, user)
            print(' v | buku berhasil di pinjam')
            return {key: book}

    print(' e | buku tidak dapat dipinjam')
    borrow_book(user, books)


def return_book(user: User, books: dict):
    print("\nKembalikan Buku")
    books_can_return = check_book(books, const.RETURN_BOOK, user)

    if books_can_return:
        book_title = input('\npilih buku : ')

        for key, book in books_can_return.items():
            if return_book == book.title or book_title == str(key):
                books[key] = Book(book.title)
                print(' v | buku berhasil di kembalikan')
                return books
    else:
        print(' e | empty borrowed books')
        return books

    print(' e | book not exist')
    return_book(user, books)


def input_book(user: User, books: dict):
    print("\nInput Buku")
    book_title = input('judul buku : ')
    already_exist = bool(check_book(books, const.INPUT_BOOK, book_title))

    if not already_exist:
        books[len(books)] = Book(book_title.title())
        print(" v | buku berhasil di inputkan")
    else:
        print(" e | book already exist")
        input_book(user, books)

    return books
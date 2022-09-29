from model.user import User
from model.book import Book

ADMIN = 'admin'
USER_ADMIN = User('zulfiqor', 'admin', role=ADMIN)

BOOKS = [
    Book("Don't Just Book By His Cover"),
    Book("Pierre"),
    Book("Piknik Seru"),
]

BORROW_BOOK = 'borrow book'
RETURN_BOOK = 'return book'
INPUT_BOOK = 'input book'

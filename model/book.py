from model.user import User


class Book:
    def __init__(self, title, borrower=User):

        self.title = title
        self.borrower = borrower

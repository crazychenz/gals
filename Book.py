import pprint

from Reservation import Reservation

class Book(object):

    books = {}

    @classmethod
    def find_book(cls, qr_code):
        # TODO: check existence
        return cls.books[qr_code]

    @classmethod
    def add_book(cls, book):
        # TODO: Check duplicates
        cls.books[book.qr_code] = book

    @classmethod
    def destroy_book(self, qr_code):
        # TODO: check existence
        del books[qr_code]

    def __init__(self, qr_code, title, bearer):
        self.qr_code = qr_code
        self.title_isbn = title.isbn
        self.bearer_uuid = bearer.uuid
        self.reservation = None

    # This is only called by kiosk (maybe admin)
    def set_bearer(self, uuid_param):
        self.bearer_uuid = uuid_param

    def reserve(self, patron_id):
        self.reservation = Reservation(patron_id, self.qr_code)




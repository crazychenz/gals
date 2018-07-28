import pprint

from Title import Title
from Bearer import Bearer
from Book import Book

class Kiosk(Bearer):

    kiosks = {}

    @classmethod
    def find_kiosk(cls, uuid):
        # TODO: check existence
        return cls.kiosks[uuid]

    @classmethod
    def add_kiosk(cls, kiosk):
        # TODO: Check duplicates
        cls.kiosks[kiosk.uuid] = kiosk
    
    # title is isbn
    @classmethod
    def get_available_book_counts(cls, title):
        counts = {}
        for kiosk in cls.kiosks.values():
            if title in kiosk.available_books_by_title:
                counts[kiosk.uuid] = len(kiosk.available_books_by_title[title])
            else:
                counts[kiosk.uuid] = 0
        return counts

    # title is isbn
    @classmethod
    def get_reserved_book_counts(cls, title):
        counts = {}
        for kiosk in cls.kiosks.values():
            if title in kiosk.reserved_books_by_title:
                counts[kiosk.uuid] = len(kiosk.reserved_books_by_title[title])
            else:
                counts[kiosk.uuid] = 0
        return counts

    def __init__(self, id):
        super(Kiosk, self).__init__(id)

        # Available
        self.available_books_by_title = {} #{1234, [5432, 5433]}

        # Reserved
        self.reserved_books_by_title = {} #{1234, [5432, 5433]}

        # Requested
        self.requests = {} # {1234, [patron1, patron2]}

        pass

    def get_title_reserved_count(title):
        return len(kiosk.reserved_books_by_title[title])

    def get_title_available_count(title):
        return len(kiosk.available_books_by_title[title])

    # Rarely executed .. ok to be suboptimal
    def list_contents(self):
        contents = {}

        for title in available_books_by_title:
            if title not in contents:
                contents[title] = {}
            contents[title]['available'] = available_books_by_title[title].copy()

        for title in available_books_by_title:
            if title not in contents:
                contents[title] = {}
            contents[title]['available'] = available_books_by_title[title].copy()

        for title in contents:
            contents[title]['object'] = Title.find_title(title)

    # qr_code -> int
    def remove_book(self, qr_code):
        pass

    # qr_code -> int
    def reserve_book(self, title_id, book_id, patron_id):
        # TODO: Check duplicates
        if title_id not in self.reserved_books_by_title:
            self.reserved_books_by_title[title_id] = []
        self.reserved_books_by_title[title_id].append(book_id)

        book = Book.find_book(book_id)
        book.reserve(patron_id)

    # qr_code -> int
    def reserve_title(self, title_id, patron_id):
        # Move book from available to reserved
        # TODO: Only do this if its last bearer was kiosk?
        book_id = self.available_books_by_title[title_id].pop()
        self.reserve_book(title_id, book_id, patron_id)

    # patron -> Patron, title -> Title
    # returns Reservation
    def get_reservation(self, patron, title):
        pass

    # patron -> Patron, title -> Title
    # returns Request
    def get_request(self, patron, title):
        pass

    # patron -> Patron, title -> title
    def request_title(self, title_id, patron_id):
        if title_id not in self.requests:
            self.requests[title_id] = []
        # TODO: Check patron duplicates
        self.requests[title_id].append(patron_id)

    def cancel_reservation(self, reservation):
        pass

    def cancel_request(self, request):
        pass

    # reservation fulfilment
    def eject_reserved_book(self, patron_id, book_id):
        # TODO: Check validity
        book = Book.find_book(book_id)
        title_id = book.title_isbn
        
        # If this doesn't work, it wasn't reserved.
        self.reserved_books_by_title[title_id].remove(book_id)

        # Set the bearer
        book.set_bearer(patron_id)

    # employee ejection (can employees eject reserved books? if so, does it cancel the reservation?)
    def eject_book(self, employee_id, book_id):
        book = Book.find_book(book_id)
        self.available_books_by_title[book.title_isbn].remove(book_id)
        book.set_bearer(employee_id)

    def has_request(self, title_id):
        if title_id in self.requests and len(self.requests[title_id]) > 0:
            return True
        return False

    def insert_book(self, qr_code):
        # TODO: check duplicates
        book = Book.find_book(qr_code)
        title_id = book.title_isbn
        book_id = book.qr_code

        # Was requested at this kiosk?
        if self.has_request(title_id):
            print self.requests
            patron_id = self.requests[title_id].pop(0)
            self.reserve_book(title_id, book_id, patron_id)
            
        else:
            if title_id not in self.available_books_by_title:
                self.available_books_by_title[title_id] = []
            self.available_books_by_title[title_id].append(qr_code)

        book.set_bearer(self.uuid)

    # ??
    def validate_credentials(self, patron):
        pass
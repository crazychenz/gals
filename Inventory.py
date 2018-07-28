class Inventory(object):
    def __init__(self):
        # Note: These are where the real object live.

        # indexed with isbn
        self.titles = {}
        # indexed with uuid
        self.kiosks = {}
        # indexed with qr_code
        self.books = {}

    def get_book_title(self, qr_code):
        return self.books[qr_code]

    # returns recusive report of all things in inventory
    def list_inventory_status(self):
        pass

    def add_kiosk(self, kiosk):
        # TODO: Check duplicates
        self.kiosks[kiosk.uuid] = kiosk

    def add_title(self, title):
        # TODO: check for duplicates
        self.titles[title.isbn] = title

    def get_title(self, isbn):
        # TODO: check for existance
        return self.titles[isbn]

    # ??
    def generateReport(self, int):
        pass
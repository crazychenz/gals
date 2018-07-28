import string

class Title(object):

    titles = {}

    @classmethod
    def find_title(cls, isbn):
        # TODO: check existence
        return cls.titles[isbn]

    @classmethod
    def add_title(cls, title):
        # TODO: Check duplicates
        cls.titles[title.isbn] = title

    @classmethod
    def keyword_search(cls, keyword):
        results = []
        for title in cls.titles.values():
            if title.keywords_match(keyword):
                results.append(title.isbn)
        return results

    def __init__(self, isbn, cover_title, cover_author):
        self.isbn = isbn
        self.cover_title = cover_title
        self.cover_author = cover_author
        # indexed with qr_code
        #self.books = []

        pass

    def keywords_match(self, keyword):
        if string.find(self.cover_title, keyword) >= 0:
            return True
        return False

    #def add_book(self, qr_code):
        # TODO: Check duplicates
    #    self.books.append(qr_code)


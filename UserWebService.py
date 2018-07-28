from Kiosk import Kiosk
from Title import Title

class UserWebService(object):
    def __init__(self, patron_id):
        self.patron_id = patron_id

    # returns list of _available_ books per kiosk
    # (since thats all the user cares about?)
    def search(self, keyword):
        results = {}
        title_ids = Title.keyword_search(keyword)
        for title_id in title_ids:
            results[title_id] = Kiosk.get_available_book_counts(title_id)
        return results

    def reserve_title(self, title_id, kiosk_id):
        kiosk = Kiosk.find_kiosk(kiosk_id)
        kiosk.reserve_title(title_id, self.patron_id)

    def request_title(self, title_id, kiosk_id):
        kiosk = Kiosk.find_kiosk(kiosk_id)
        kiosk.request_title(title_id, self.patron_id)
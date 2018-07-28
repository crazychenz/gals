import uuid

class Reservation(object):
    def __init__(self, patron_id, book_id, uuid_param = None):
        self.patron_id = patron_id
        self.book_id = book_id

        # TODO: Track reservation time to pickup
        # TODO: Track pickup time to return time

        if uuid_param is None:
            self.uuid = uuid.uuid4()
        else:
            self.uuid = uuid_param
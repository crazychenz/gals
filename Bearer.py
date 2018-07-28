import uuid

# Base class for anything that can bear a book
class Bearer(object):
    def __init__(self, uuid_param = None):
        if uuid_param is None:
            self.uuid = uuid.uuid4()
        else:
            self.uuid = uuid_param
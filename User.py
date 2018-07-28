from Bearer import Bearer

class User(Bearer):
    def __init__(self, name):
        super(User, self).__init__()
        self.name = name
        pass
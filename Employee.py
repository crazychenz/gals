from User import User

class Employee(User):
    def __init__(self, name):
        super(Employee, self).__init__(name)
        pass
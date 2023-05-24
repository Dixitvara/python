# pickle and unpickle in python
class emp:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print("{:5d} {:10s} {:10.2}".format(self.id, self.name, self.salary))
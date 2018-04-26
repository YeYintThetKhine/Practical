class Guitar:
    def __init__(self, name='', year=0, cost=0):
        self.name=name
        self.year= year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        self.age =  2017 - self.year
        return self.age

    def is_vintage(self):
        return self.get_age() >= 50



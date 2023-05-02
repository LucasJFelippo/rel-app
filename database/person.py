# Main Object of the users
class Person():
    def __init__(self, personId, personName, personAge, personElo):
        self.id = personId
        self.name = personName
        self.age = personAge
        self.likes = []
        self.elo = personElo
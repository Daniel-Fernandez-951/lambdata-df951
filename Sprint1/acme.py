"""
Part 1- Keeping it Classy
"""

from random import randint


class Product:

    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=randint(1000000, 9999999)):
        self.name = str(name)
        self.price = int(price)
        self.weight = int(weight)
        self.flammability = float(flammability)
        self.identifier = identifier

    def stealability(self):
        ratio = self.price / self.weight
        if ratio < 0.5:
            return "Not so stealable"
        elif 1 > ratio >= 0.5:
            return "Kinda stealable"
        else:
            return "Very stealable"

    def explode(self):
        f_rate = self.flammability * self.weight
        if f_rate < 10:
            return ". . .fizzle"
        elif 10 <= f_rate < 50:
            return ". . .boom"
        else:
            return ". . .BABOOM!!"

class BoxingGlove(Product):

    def __init__(self, name, price=10, weight=10, flammability=0.5, identifier=randint(1000000, 9999999)):
        super().__init__(name, price, weight, flammability, identifier)
        self.weight = weight

    def explode(self):
        return ". . .it's a glove"

    def punch(self, weight):
        if weight < 5:
            return "That tickles"
        elif 5 <= weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"

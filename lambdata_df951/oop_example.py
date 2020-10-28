"""
OOP examples Module 2
"""

import pandas as pd
import numpy as np

class MyDataFrame(pd.DataFrame):
    def num_cells(self):
        return self.shape[0] * self.shape[1]


class BareMinimumClass:
    pass

class Complex:
    def __init__(self, realpart, imagpart):
        """
        Constructor for complex numbers.
        Complex numbers have a real part and an imaginary part.
        """
        self.r = realpart
        self.i = imagpart

    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i

    def __repr__(self):
        return '({}, {})'.format(self.r, self.i)\

class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)

    def recieve_upvotes(self, num_upvotes=1):
        self.upvotes += num_upvotes

    def is_popular(self):
        return self.upvotes > 100


class Animal:
    """General representation of an animal"""
    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = float(weight)
        self.diet_type = str(diet_type)

    def run(self):
        return "Vroom, Vroom, I go Quick!"

    def eat(self, food):
        return f"Huge fan of that {str(food)}"


class Sloth(Animal):
    def __init__(self, name, weight, diet_type, num_naps):
        # Use from Animals
        super().__init__(name, weight, diet_type)
        self.num_naps = int(num_naps)

    def say_something(self):
        return "Almost there, just one more step!"

    def run(self):
        return "Brutally Slow"



if __name__ == '__main__':
    num1 = Complex(3, 5)
    num2 = Complex(4, 2)
    num1.add(num2)
    print(num1.r, num2.i)

    user1 = SocialMediaUser("Daniel", "Texas", 100)
    user2 = SocialMediaUser("Nick", "Logan", 2)
    user3 = SocialMediaUser(name="Carl", location="Mexico", upvotes=99)
    user4 = SocialMediaUser(name="Bob Bill", location="Utah", upvotes=4)
    print(f'{user4.name} is popular {user4.is_popular()}, # up-votes: {user4.upvotes}')
    print(f'{user3.name} is popular {user3.is_popular()}, # up-votes: {user3.upvotes}')
# Static Methods imported from respective files
from Addition import addition
from Subtraction import subtraction
from Multiplication import multiplication
from Division import division
from Squareroot import squareroot


class Calculator:
    result = 0

    def __init__(self):
        pass

# Functions
    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = multiplication(a, a)
        return self.result

    def squareroot(self, a):
        self.result = squareroot(a)
        return self.result

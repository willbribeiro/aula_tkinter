import math

class ScientificCalculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error: Division by zero"
        return x / y

    def exponentiate(self, x, y):
        return x ** y

    def square_root(self, x):
        if x < 0:
            return "Error: Square root of a negative number"
        return math.sqrt(x)

    def factorial(self, x):
        if x < 0:
            return "Error: Factorial of a negative number"
        return math.factorial(x)

    def sine(self, x):
        return math.sin(x)

    def cosine(self, x):
        return math.cos(x)

    def tangent(self, x):
        return math.tan(x)

    def logarithm(self, x, base):
        if x <= 0 or base <= 0 or base == 1:
            return "Error: Invalid input for logarithm"
        return math.log(x, base)

# Example usage:
calculator = ScientificCalculator()

print("1 + 2 =", calculator.add(1, 2))
print("5 - 3 =", calculator.subtract(5, 3))
print("2 * 4 =", calculator.multiply(2, 4))
print("6 / 3 =", calculator.divide(6, 3))
print("3 ^ 4 =", calculator.exponentiate(3, 4))
print("Square root of 25 =", calculator.square_root(25))
print("Factorial of 5 =", calculator.factorial(5))
print("Sine of 0 =", calculator.sine(0))
print("Cosine of 0 =", calculator.cosine(0))
print("Tangent of 0 =", calculator.tangent(0))
print("Log base 10 of 1000 =", calculator.logarithm(1000, 10))

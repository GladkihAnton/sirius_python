# Создайте классы Addition, Subtraction, Multiplication, Division.
# У каждого есть метод calculate(a, b), который выполняет соответствующую операцию.
#
# Создайте функцию run_operation(operation, a, b), которая вызывает метод calculate у переданного объекта.
#
# Как пример необходимо составить уравнение 3 + 3 * 3 + 4 / 2 - 10
from abc import ABC


class Calculator(ABC):
    def calculate(self, a, b):
        raise NotImplementedError


class Plus(Calculator):
    def calculate(self, a, b):
        return a + b


class Minus(Calculator):
    def calculate(self, a, b):
        return a - b


class Multiply(Calculator):
    def calculate(self, a, b):
        return a * b


class Devide(Calculator):
    def calculate(self, a, b):
        return a / b


def run_operation(operation: Calculator, a: int, b: int):
    return operation.calculate(a, b)


# 3 + 3 * 3 + 4 / 2 - 10
run_operation(Multiply(), 3, 3)
# 3 + 3 * 3
run_operation(Plus(), 3, run_operation(Multiply(), 3, 3))

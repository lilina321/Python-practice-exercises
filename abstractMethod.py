from abc import ABC, abstractmethod
import math

class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Figure):

    def __init__(self, a = 1):
        self.a = a

    def area(self):
        return self.a * self.a

    def perimeter(self):
        return self.a * 4


class Circle(Figure):

    def __init__(self, radius = 1):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Figure):

    def __init__(self, a, b, c, height):
        self.b = b
        self.height = height
        self.a = a
        self.c = c

    def area(self):
        return self.b * self.height / 2

    def perimeter(self):
        return self.a + self.b + self.c

listOfFigures = [Square(), Square(2), Square(5), Circle(1), Circle(2), Circle(5), Triangle(1, 2, 3, 1)]

for square in listOfFigures:
    print('Area:', round(square.area(), 2))
    print('Perimeter:', round(square.perimeter(), 2), '\n')


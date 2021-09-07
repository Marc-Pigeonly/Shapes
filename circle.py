from base_shape import Shape
import math


class Circle(Shape):

    def __init__(self, radius):
        self._radius = radius
        self._diameter = 2 * radius

    def area(self):
        return math.pi * self._radius * self._radius

    def perimeter(self):
        return 2 * math.pi * self._radius
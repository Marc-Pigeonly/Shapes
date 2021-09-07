import math


class Circle:

    def __init__(self, radius):
        self._radius = radius
        self._diameter = 2 * radius

    @property
    def radius(self):
        """
        Radius of a Circle
        :return: The radius of the circle instance
        :rtype: float
        """
        return float(self._radius)

    def area(self):
        """
        Area of a Circle
        :return: The area of the circle instance
        :rtype: float
        """
        return self.area_of_a_circle(self.radius)

    def perimeter(self):
        """
        Perimeter of a Circle
        :return: The perimeter of a circle instance
        :rtype: float
        """
        return self.perimeter_of_a_circle(self.radius)

    @staticmethod
    def area_of_a_circle(radius):
        """
        Function to calculate the area of a circle with a given radius
        area = PI * R^2
        :param radius: The radius of the circle
        :type: float
        :return: The area of a circle with a given radius
        :rtype: float
        """
        if isinstance(radius, float):
            return math.pi * (radius * radius)
        else:
            raise TypeError("Radius not given as a float")

    @staticmethod
    def perimeter_of_a_circle(radius):
        """
        Function to calculate the perimeter of a circle with a given radius
        perimeter = 2PI * R
        :param radius: The radius of the circle
        :type: float
        :return: The area of a perimeter with a given radius
        :rtype: float
        """
        if isinstance(radius, float):
            return 2 * math.pi * radius
        else:
            raise TypeError("Radius not given as a float")

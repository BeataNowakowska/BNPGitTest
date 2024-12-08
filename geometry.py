import math

class Geometry:
    def __init__(self):
        pass

    def rectangle_area(self, width, height):
        """Oblicza pole prostokąta"""
        return width * height

    def rectangle_perimeter(self, width, height):
        """Oblicza obwód prostokąta"""
        return 2 * (width + height)

    def circle_area(self, radius):
        """Oblicza pole koła"""
        return math.pi * radius ** 2

    def circle_circumference(self, radius):
        """Oblicza obwód koła"""
        return 2 * math.pi * radius

    def triangle_area(self, base, height):
        """Oblicza pole trójkąta"""
        return 0.5 * base * height

    def triangle_perimeter(self, a, b, c):
        """Oblicza obwód trójkąta"""
        return a + b + c

    def square_area(self, side):
        """Oblicza pole kwadratu"""
        return side ** 2

    def square_perimeter(self, side):
        """Oblicza obwód kwadratu"""
        return 4 * side

    def trapezoid_area(self, a, b, height):
        """Oblicza pole trapezu"""
        return 0.5 * (a + b) * height

    def trapezoid_perimeter(self, a, b, c, d):
        """Oblicza obwód trapezu"""
        return a + b + c + d

# Przykład użycia
geometry = Geometry()
print("Usage example")

print("Rectangle area:", geometry.rectangle_area(5, 10))
print("Rectangle perimeter:", geometry.rectangle_perimeter(5, 10))

# Circle
print("Circle area:", geometry.circle_area(7))
print("Circle circumference:", geometry.circle_circumference(7))

# Triangle
print("Triangle area:", geometry.triangle_area(6, 8))
print("Triangle perimeter:", geometry.triangle_perimeter(3, 4, 5))

# Square
print("Square area:", geometry.square_area(4))
print("Square perimeter:", geometry.square_perimeter(4))

# Trapezoid
print("Trapezoid area:", geometry.trapezoid_area(5, 10, 6))
print("Trapezoid perimeter:", geometry.trapezoid_perimeter(5, 10, 4, 7))

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

# Przykład użycia
geometry = Geometry()

# Prostokąt
print("Pole prostokąta:", geometry.rectangle_area(5, 10))
print("Obwód prostokąta:", geometry.rectangle_perimeter(5, 10))

# Koło
print("Pole koła:", geometry.circle_area(7))
print("Obwód koła:", geometry.circle_circumference(7))

# Trójkąt
print("Pole trójkąta:", geometry.triangle_area(6, 8))
print("Obwód trójkąta:", geometry.triangle_perimeter(3, 4, 5))

# Kwadrat
print("Pole kwadratu:", geometry.square_area(4))
print("Obwód kwadratu:", geometry.square_perimeter(4))

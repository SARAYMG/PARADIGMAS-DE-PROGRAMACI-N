from math import pi, sqrt

class Figure:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def perimeter(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def area(self):
        raise NotImplementedError("Subclasses should implement this method.")

class Triangle(Figure):
    def __init__(self, color, a, b, c):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

class Circle(Figure):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def perimeter(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius ** 2

class Rectangle(Figure):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

class Hexagon(Figure):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def perimeter(self):
        return 6 * self.side

    def area(self):
        return (3 * sqrt(3) * (self.side ** 2)) / 2

# Demostración de polimorfismo
figures = [
    Triangle("Rojo", 3, 4, 5),
    Circle("Azul", 2.5),
    Rectangle("Verde", 4, 6),
    Hexagon("Amarillo", 2)
]

for figure in figures:
    print(f"Color: {figure.get_color()}")
    print(f"Perimetro: {figure.perimeter()}")
    print(f"Area: {figure.area()}")
    print()

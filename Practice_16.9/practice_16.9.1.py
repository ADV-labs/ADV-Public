print(".........")

class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h
    def __str__(self):
        return f'Прямоугольник (ширина = {self.width}, высота = {self.height})'

class Square:
    def __init__(self, s):
        self.side = s
    def __str__(self):
        return f'Квадрат (ширина = {self.side}, высота = {self.side})'


class Circle:
    def __init__(self, r):
        self.radius = r
    def __str__(self):
        return f'Окружность (радиус = {self.radius})'

class Triangle:
    def __init__(self, a, b, c):
        self.side_a = a
        self.side_b = b
        self.side_c = c
    def __str__(self):
        return f'Треугольник (сторона a = {self.side_a}, сторона b = {self.side_b}, сторона c = {self.side_c})'

rectangle = Rectangle(3, 6)
square = Square(12)
circle = Circle(22)
triangle = Triangle(7, 5, 9)

print(rectangle)
print(square)
print(circle)
print(triangle)

print(".........")
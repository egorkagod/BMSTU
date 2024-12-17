from rectangle import Rectangle
from circle import Circle
from square import Square

if __name__ == "__main__":
    N = 5  # Подставьте значение N, если оно известно, иначе используйте для тестов

    rectangle = Rectangle(N, N, "blue")
    circle = Circle(N, "green")
    square = Square(N, "red")

    print(rectangle)
    print(circle)
    print(square)

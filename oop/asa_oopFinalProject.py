from abc import ABC, abstractmethod
from math import sqrt


# Ahmed Dusuki : Triangle, EquilateralTriangle, IsoscelesTriangle, Hexagon classes; user input validation
# Ahmed Ashraf : Quadrilateral, Rectangle, Square, Pentagon classes
# Mostafa Mohamed : Polygon, Octagon classes, main while loop


class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Triangle(Polygon):
    def __init__(self, height, base):
        self.__height = height
        self.__base = base

    def area(self):
        return 0.5 * self.__base * self.__height

    @abstractmethod
    def draw(self):
        pass


class EquilateralTriangle(Triangle):
    def __init__(self, base):
        super().__init__((base * sqrt(3)) / 2, base)

    def perimeter(self):
        return self._Triangle__base * 3

    def draw(self):
        spaces = self._Triangle__base - 1
        print(" " * spaces + "*")
        spaces -= 1
        for i in range(self._Triangle__base - 2):
            print(" " * spaces + "*", end="")
            print(" " * (1 + i * 2), end="")
            print("*")
            spaces -= 1
        if spaces == 0:
            print("* " * self._Triangle__base)


class IsoscelesTriangle(Triangle):
    def __init__(self, height, base):
        super().__init__(height, base)

    def perimeter(self):
        side = sqrt(pow(self._Triangle__base / 2, 2) + pow(self._Triangle__height, 2))
        return 2 * side + self._Triangle__base

    def draw(self):
        for i in range(1, self._Triangle__height + 1):
            stars = max(1, round(i * self._Triangle__base / self._Triangle__height))
            spaces = self._Triangle__base - stars
            print(" " * spaces + "* " * stars)


class Quadrilateral(Polygon):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return (self.__length + self.__width) * 2

    @abstractmethod
    def draw(self):
        pass


class Rectangle(Quadrilateral):
    def __init__(self, length, width):
        super().__init__(length, width)

    def draw(self):
        for i in range(self._Quadrilateral__length):
            for j in range(self._Quadrilateral__width):
                print("*", end="  ")
            print()


class Square(Quadrilateral):
    def __init__(self, side):
        super().__init__(side, side)

    def draw(self):
        for i in range(self._Quadrilateral__length):
            for j in range(self._Quadrilateral__width):
                print("*", end="  ")
            print()


class Pentagon(Polygon):
    def __init__(self, side):
        self.__side = side

    def perimeter(self):
        return self.__side * 5

    def area(self):
        return 0.25 * sqrt(5 * (5 + 2 * sqrt(5))) * pow(self.__side, 2)

    def draw(self):
        for i in range(1, self.__side + 1):
            for space in range((self.__side * 2) - (2 * i), 0, -1):
                print(" ", end="")
            for star in range(2 * i - 1):
                print("* ", end="")
            print()
        for i in range(1, self.__side):
            for space in range(i):
                print(" ", end="")
            for star in range((self.__side * 2) - 1 - i, 0, -1):
                print("* ", end="")
            print()


class Hexagon(Polygon):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return (3 * sqrt(3) * pow(self.__side, 2)) / 2

    def perimeter(self):
        return self.__side * 6

    def draw(self):
        print("  " * max((self.__side - 1), 1) + "*")
        spaces = 3
        for i in range(self.__side - 2, 0, -1):
            print("  " * i + "*" + " " * spaces + "*")
            spaces += 4

        for i in range(self.__side):
            print("*" + " " * spaces + "*")

        spaces -= 4
        for i in range(1, self.__side - 1):
            print("  " * i + "*" + " " * spaces + "*")
            spaces -= 4
        print("  " * max((self.__side - 1), 1) + "*")


class Octagon(Polygon):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return 2 * pow(self.__side, 2) * (1 + sqrt(2))

    def perimeter(self):
        return self.__side * 8

    def draw(self):
        for i in range(self.__side):
            print("  " * (self.__side - i - 1) + "* " * (self.__side + i * 2))
        for i in range(self.__side - 1):
            print("* " * (self.__side + (self.__side - 1) * 2))
        for i in range(self.__side - 2, -1, -1):
            print("  " * (self.__side - i - 1) + "* " * (self.__side + i * 2))


while True:
    print(
        "\n1. Equilateral triangle\n2. Isosceles triangle\n3. Rectangle\n4. Square\n5. Pentagon\n6. Hexagon\n7. Octagon\n8. Exit\n"
    )

    choice = input(("Enter desired option: "))
    while not choice.isnumeric() or int(choice) < 1 or int(choice) > 8:
        choice = input(("Enter valid option: "))
    choice = int(choice)

    if choice == 1:
        side = input("Enter side length: ")
        while not side.isnumeric() or int(side) < 1:
            side = input("Enter side length (positive integer): ")
        side = int(side)

        equilateral = EquilateralTriangle(side)
        print("\nThe shape perimeter is: " + str(equilateral.perimeter()))
        print("The shape area is: " + str(equilateral.area()))
        print("The shape drawing:")
        equilateral.draw()
    elif choice == 2:
        height = input("Enter height length: ")
        while not height.isnumeric() or int(height) < 1:
            height = input("Enter height length (positive integer): ")
        height = int(height)

        base = input("Enter base length: ")
        while not base.isnumeric() or int(base) < 1:
            base = input("Enter base length (positive integer): ")
        base = int(base)

        isosceles = IsoscelesTriangle(height, base)
        print("\nThe shape perimeter is: " + str(isosceles.perimeter()))
        print("The shape area is: " + str(isosceles.area()))
        print("The shape drawing:")
        isosceles.draw()
    elif choice == 3:
        length = input("Enter rectangle length: ")
        while not length.isnumeric() or int(length) < 1:
            length = input("Enter rectangle length (positive integer): ")
        length = int(length)

        width = input("Enter rectangle width: ")
        while not width.isnumeric() or int(width) < 1:
            width = input("Enter rectangle width (positive integer): ")
        width = int(width)

        rectangle = Rectangle(length, width)
        print("\nThe shape perimeter is: " + str(rectangle.perimeter()))
        print("The shape area is: " + str(rectangle.area()))
        print("The shape drawing:")
        rectangle.draw()
    elif choice == 4:
        side = input("Enter side length: ")
        while not side.isnumeric() or int(side) < 1:
            side = input("Enter side length (positive integer): ")
        side = int(side)

        square = Square(side)
        print("\nThe shape perimeter is: " + str(square.perimeter()))
        print("The shape area is: " + str(square.area()))
        print("The shape drawing:")
        square.draw()
    elif choice == 5:
        side = input("Enter side length: ")
        while not side.isnumeric() or int(side) < 1:
            side = input("Enter side length (positive integer): ")
        side = int(side)

        pentagon = Pentagon(side)
        print("\nThe shape perimeter is: " + str(pentagon.perimeter()))
        print("The shape area is: " + str(pentagon.area()))
        print("The shape drawing:")
        pentagon.draw()
    elif choice == 6:
        side = input("Enter side length: ")
        while not side.isnumeric() or int(side) < 1:
            side = input("Enter side length (positive integer): ")
        side = int(side)

        hexagon = Hexagon(side)
        print("\nThe shape perimeter is: " + str(hexagon.perimeter()))
        print("The shape area is: " + str(hexagon.area()))
        print("The shape drawing:")
        hexagon.draw()
    elif choice == 7:
        side = input("Enter side length: ")
        while not side.isnumeric() or int(side) < 1:
            side = input("Enter side length (positive integer): ")
        side = int(side)

        octagon = Octagon(side)
        print("\nThe shape perimeter is: " + str(octagon.perimeter()))
        print("The shape area is: " + str(octagon.area()))
        print("The shape drawing:")
        octagon.draw()
    elif choice == 8:
        print("Exiting..")
        break

""" Super () = Function used to give access to the methods of
a parent class.
Return a temporary objects of a parent class when used
 """


class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length


class Square(Rectangle):
    def __init__(self, width, length):
        super().__init__(width, length)

    #   self.length = length
    # self.width = width
    def area(self):
        return self.length * self.width


class Cube(Rectangle):
    def __init__(self, length, width, height):
        self.height = height
        super().__init__(length, width)

    def volume(self):
        return self.length * self.width * self.height + 12
    # self.width = width
    # self.height = height


square = Square(3, 3)
cube = Cube(3, 3, 3)

print(cube.volume())
print(square.area())

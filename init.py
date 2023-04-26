class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# create a rectangle with width=5 and height=3
rect = Rectangle(5, 3)

# print the area and perimeter of the rectangle
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, alt_width):
        self.width = alt_width

    def set_height(self, alt_height):
        self.height = alt_height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width**2 + self.height**2) ** 0.5
        return diagonal

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return f"Too big for picture."

        output_picture = [self.width * "*" for _ in range(self.height)]
        return "\n".join(output_picture) + "\n"

    def get_amount_inside(self, other):
        amount_inside = int(self.get_area() / other.get_area())
        return amount_inside


class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, alt_side):
        self.width = alt_side
        self.height = alt_side

    def set_width(self, alt_width):
        self.width = alt_width
        self.height = alt_width

    def set_height(self, alt_height):
        self.width = alt_height
        self.height = alt_height


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

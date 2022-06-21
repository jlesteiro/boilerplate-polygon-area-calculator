class Rectangle:

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def __repr__(self):
        repr_string = "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
        return repr_string

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_area(self):
        return (self.height * self.width)

    def get_perimeter(self):
        return (2*self.width + 2*self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture_str = str()
            for fila in range(self.height):
                for col in range(self.width):
                    picture_str += "*"
                picture_str += "\n"
            return picture_str

    def get_amount_inside(self, child):
        how_many_heights = int(self.height / child.height)
        how_many_widhts = int(self.width / child.width)
        return how_many_heights * how_many_widhts


class Square(Rectangle):

    def __init__(self, s):
        super().__init__(s, s)

    def __repr__(self):
        repr_string = "Square(side=" + str(self.width) + ")"
        return repr_string

    def set_side(self, s):
        self.height = s
        self.width = s

    def set_height(self, h):
        self.height = h
        self.width = h

    def set_width(self, w):
        self.height = w
        self.width = w
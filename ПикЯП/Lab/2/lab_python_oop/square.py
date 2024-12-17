from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side, color_name):
        super().__init__(side, side, color_name)

    def __repr__(self):
        return "Square(color: {}, side: {}, area: {:.2f})".format(
            self.color.color_name, self.width, self.area()
        )

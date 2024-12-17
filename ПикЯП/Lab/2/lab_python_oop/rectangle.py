from geometric_figure import GeometricFigure
from color import Color

class Rectangle(GeometricFigure):
    def __init__(self, width, height, color_name):
        self.width = width
        self.height = height
        self.color = Color(color_name)

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "Rectangle(color: {}, width: {}, height: {}, area: {:.2f})".format(
            self.color.color_name, self.width, self.height, self.area()
        )

import abc
from Predictive_analysis import Predictive_Analysis

class Model(metaclass=abc.ABCMeta):
    
    def __init__(self, model):
        self.model = model
        pass
    
    @abc.abstractstaticmethod
    def set_model(self):
        pass
    
class Model_type():
    pass
    

class Color(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fill_color(self):
        pass

class Shape(metaclass=abc.ABCMeta):
    def __init__(self, color):
        self.color = color

    @abc.abstractmethod
    def color_it(self):
        pass

class Rectangle(Shape):
    def __init__(self, color):
        super(Rectangle, self).__init__(color)

    def color_it(self):
        print("Rectangle filled with ", end="")
        self.color.fill_color()


class RedColor(Color):
    def fill_color(self):
        print("red color")


if __name__ == '__main__':
    s1 = Rectangle(RedColor())
    s1.color_it()

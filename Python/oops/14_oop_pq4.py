from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self, r):
        self.r = r

    def area(self):
        ar = 3.14*self.r**2
        return ar

class Rectangle(Shape):

    def __init__(self,l,b):
        self.l = l
        self.b = b

    def area(self):
        ar = self.l * self.b
        return ar

class Triangle(Shape):

    def __init__(self, base, h):
        self.base = base
        self.h = h

    def area(self):
        ar = 0.5 * self.base * self.h
        return ar

s1 = Triangle(5,2)
print(s1.area())

s2 = Rectangle(2,3)
print(s2.area())

s3 = Circle(5)
print(s3.area())


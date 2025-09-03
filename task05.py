class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, yuzi):
        self.yuzi = yuzi
    
    def area(self):
        pi = 3.14159
        S = pi * (self.yuzi ** 2)
        return S

class Restangle(Shape):
    def __init__(self, eni, boyi):
        self.eni = eni
        self.boyi = boyi
    def area(self):
        s = self.eni * self. boyi
        return s

c = Circle(5)
r = Restangle(4, 6)
print(c.area())
print(r.area())
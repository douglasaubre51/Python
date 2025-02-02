import math

class Shape:
    def __init__ (self,name):
        self.name=name

    def getShape(self):
        print(f"the shape is {self.name}")

class Circle(Shape):
    def __init__(self,name,radius):
        super().__init__(name)
        self.radius=radius

    def getArea(self):
        return math.pi*self.radius**2

class Square(Shape):
    def __init__(self,name,side):
        super().__init__(name)
        self.side=side

    def getArea(self):
        return self.side**2

circle=Circle('Circle',5)
circle.getShape()
print(f'area : {circle.getArea()}')

square=Square('Square',4)
square.getShape()
print(f'area : {square.getArea()}')
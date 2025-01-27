class Box:
    length=0
    breadth=0
    height=0
    area=0
    volume=0

    def __init__(self,l,b,h):
        self.length=l
        self.breadth=b
        self.height=h
        
    def calculateArea(self):
        self.area=self.length*self.breadth*self.height

    def getArea(self):
        print(f"area of box:{self.area}")
    
print('Box')
l=int(input("enter length:"))
b=int(input("enter breadth:"))
h=int(input("enter height:"))

box=Box(l,b,h)

box.calculateArea()
box.getArea()

print('bye')
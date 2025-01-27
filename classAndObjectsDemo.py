class Room:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def getArea(self):
        return self.length * self.breadth

bedRoom=Room(10,10)
print(f'area of bed room:{bedRoom.getArea()}')
hall=Room(5,10)
print(f'area of hall:{hall.getArea()}')
diningRoom=Room(2,4)
print(f'area of dining room:{diningRoom.getArea()}')
kitchen=Room(40,10)
print(f'area of kitchen:{kitchen.getArea()}')
class Animal:
    name=''

    def __init__(self,name):
        self.name=name

    def display(self):
        print(f'i am {self.name}')

    def eat(self):
        pass

class Dog(Animal):
    food=''

    def __init__(self,name,food):
        super().__init__(name)
        self.food=food

    def eat(self):
        print(f'i eat {self.food}')

rotweiler=Dog('johnny','meat')
rotweiler.display()
rotweiler.eat()
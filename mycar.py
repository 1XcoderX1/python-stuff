class Vehicle():

    def __init__(self, name, color='silver'):
        self.name = name
        self.color = color

    def getName(self):
        return self.name

    def getColor(self):
        return self.color



class Car(Vehicle):

    def getColor(self):
        self.color = "black"
        return self.color

audi = Car("Audi R8")
print("The name of your car is: " + audi.getName() + ' and the color is ' + audi.getColor())

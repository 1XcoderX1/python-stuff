class Vehicle():

    def __init__(self, brand_name, color):
        self.brand_name = brand_name
        self.color = color

    def get_brand_name(self):
        return self.brand_name

class Cost():

    def __init__(self, cost):
        self.cost = cost

    def get_cost(self):
        return self.cost

class Car(Vehicle, Cost):

    def __init__(self, brand_name, model, color, cost):
        self.model = model
        Vehicle.__init__(self, brand_name, color)
        Cost.__init__(self, cost)
        self.__engine = '5.2L V10'

    def get_description(self):
        return self.get_brand_name() + self.model + " is the car " + "and it's cost is " + self.cost

audi = Car("Audi ", "R8", "Red", "2 cr")
print("Car description: ", audi.get_description())
print("Accessing private engine: ", audi._Car__engine)

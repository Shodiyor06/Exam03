class Vehicle:
    def engine(self):
        pass
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.name = "car"
    def engine(self):
        return f"{self.name} engine started"
    
class Bike(Vehicle):
    def __init__(self):
        super().__init__()
        self.name = "bike"
    def engine(self):
        return f"{self.name} engine started"

car = Car()
bike = Bike()
print(car.engine())
print(bike.engine())
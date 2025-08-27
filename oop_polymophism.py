# assignment 2 OOP (poymophism)
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

class Boda:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Ride!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")
boda1 = Boda("TVS", "360")

for x in(car1, boat1, plane1, boda1):
    x.move()
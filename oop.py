# Assignment 1

class SmartPhone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def phone(self):
        print(f"{self.model} is a model of {self.brand}")


# Child class inheriting from SmartPhone
class Kadunda(SmartPhone):
    def __init__(self, brand, model, year):
        super().__init__(brand, model)   # Call parent constructor
        self.manufacture_year = year

    # Overriding parent method (Polymorphism)
    def phone(self):
        print(f"{self.model} is a model of {self.brand}, manufactured in {self.manufacture_year}")


# Create objects
phone_1 = SmartPhone("Samsung", "Galaxy A03")
phone_1.phone()

phone_2 = Kadunda("Motorolla", "Motorolla 123x", 1910)
phone_2.phone()



class Vehicle:
    color= "Blue"
    type = "Electric"

    def __init__(self, genre):
        self.genre = genre
        


class Car(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Bike(Vehicle):
    def __init__(self, brand, milage):
        self.brand = brand
        self.milage = milage


b1 = Bike("Yamaha", 16)

print(b1.genre)

print(f"It's a {b1.color} color {b1.type} {b1.brand} R2, which gives a milage of {b1.milage}.")
class Car:

    name = "None"
    weight = 1000
    speed = 200.00

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        print(self.name, " has weight ", self.weight)

    def set(self, name, weight, speed):
        self.name = name
        self.weight = weight
        self.speed = speed

class Truck(Car):
    wheels=8

    def __init__(self):
        pass

man = Truck()
man.wheels = 12
man.set("Man", 4500, 140.5)
print(man.name, man.wheels)

audi = Car("Audi", 1450)
audi.set("Audi", 1450, 320.30)
print(audi.name)

shkoda = Car("Shkoda", 1300)
shkoda.set("Shkoda", 1300, 235.30)
print(shkoda.name)
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


class car(Vehicle):
    def seating_capacity(self, capacity=4):
        return super().seating_capacity(capacity=4)


audi = car("q7", 280, 25)
print(audi.seating_capacity())

school_bus = bus("VOLVO", 250, 18)
print(school_bus.seating_capacity())

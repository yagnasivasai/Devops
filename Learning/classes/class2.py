class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


bus_object = Bus("qaz", 30, 35)
print(bus_object.name, bus_object.mileage, bus_object.max_speed)

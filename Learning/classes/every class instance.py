class vehicle:
    color = "white"

    def __init__(self, name, max_speed, milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage


class Bus(vehicle):
    pass


class Car(vehicle):
    pass


schoolbus = Bus("volvo", 200, 15)
print(schoolbus.color, schoolbus.name, schoolbus.max_speed, schoolbus.milage)

supercar = Car("BEnz", 250, 18)
print(supercar.color, supercar.name, supercar.milage, supercar.milage)


print(type(schoolbus))
print(isinstance(schoolbus, vehicle))

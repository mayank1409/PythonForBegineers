class MotorBike:
    def __init__(self, gears, speed):
        self.gears = gears
        self.speed = speed

    def __repr__(self):
        return repr(
            (self.gears, self.speed)
        )
    
honda = MotorBike(4, 80)
ducati = MotorBike(3, 65)

print(honda)
print(ducati)
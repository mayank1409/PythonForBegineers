class Planet:
    def __init__(self,name , distance_from_sun):
        self.name = name
        self.distance_from_sun = distance_from_sun


earth = Planet('Earth', 500)
mars = Planet('Mars', 4000)

earth.speed = 10000000
print(earth.speed)

#print(mars.speed) - AttributeError: 'Planet' object has no attribute 'speed'

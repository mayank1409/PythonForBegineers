class WaterAnimal:
    def swim(self):
        print("I can Swim")

class LandAnimal:
    def walk(self):
        print("I can walk")
    

class Amphibian(WaterAnimal, LandAnimal):
    pass


frog = Amphibian()

frog.swim()
frog.walk()
from abc import ABC, abstractmethod

class AbstractRecipe(ABC):
    def execute(self):
        self.get_ready()
        self.do_the_dish()
        self.do_clean_up()

    @abstractmethod
    def get_ready(self):
        pass


    @abstractmethod
    def do_the_dish(self):
        pass


    @abstractmethod
    def do_clean_up(self):
        pass


# recipe = AbstractRecipe() TypeError: Can't instantiate abstract class AbstractRecipe with abstract methods do_clean_up, do_the_dish, get_ready

class Recipe1(AbstractRecipe):

    def get_ready(self):
        print("Get the Raw materials")
        print("Get Utensils")

    def do_the_dish(self):
        print("DO the dishes")

    def do_clean_up(self):
        print("clean utensils")


class RecipeWithMW(AbstractRecipe):

    def get_ready(self):
        print("Get the Raw meterials")
        print("Switch on Microwave")

    def do_the_dish(self):
        print("Get Stuff ready")
        print("Put it in microwave")

    def do_clean_up(self):
        print("clean utensils")
        print("Switch off the microwave")


recipe1 = Recipe1()
recipe1.execute()

print("DONE!!!")

recipe2 = RecipeWithMW()
recipe2.execute()

print("DONE!!!")
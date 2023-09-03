from abc import ABC, abstractmethod

class GamingConsole(ABC):
    @abstractmethod
    def up(self):
        pass

    @abstractmethod
    def down(self):
        pass

    
    @abstractmethod
    def left(self):
        pass


    @abstractmethod
    def right(self):
        pass


class MarioGame(GamingConsole):
    def up(self):
        print("Runnnn....")


    def down(self):
        print('Sit Down')

    
    def left(self):
        pass

    def right(self):
        print("Fire")


class ChessGame(GamingConsole):
    def up(self):
        print("Move piece up")


    def down(self):
        print('Move piece back')

    
    def left(self):
        print('Move piece left')

    def right(self):
        print('Move piece right')


games = [MarioGame(), ChessGame()]

#Polymorphism (Duck Typing)
class  Test1:
    def method(self): print("Test1")

class Test2:
    def method(self): print("Test2")

tests = [Test1(), Test2()]

for test in tests:
    test.method()
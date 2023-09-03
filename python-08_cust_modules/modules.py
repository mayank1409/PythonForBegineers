def method():
    print('I\'m a method')


class ClassA:

    @staticmethod
    def class_method_A():
        print('I\'m a method of Class A')


# print(__name__)


if __name__ == '__main__':
    method()
    ClassA.class_method_A()

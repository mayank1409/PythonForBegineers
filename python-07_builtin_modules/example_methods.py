from collections import namedtuple

def example_method(mandatory_parameter, default_parameter='Default Parameter', *args, **kwargs):
    print(f'mandatory_parameter = {mandatory_parameter} and type = {type(mandatory_parameter)}')
    print(f'default_parameter = {default_parameter} and type = {type(default_parameter)}')
    print(f'args = {args} and type = {type(args)}')
    print(f'kwargs = {kwargs} and type = {type(kwargs)}')


example_method('Hello World')
print('#'*50)
example_method(15)
print('#'*50)
example_method(25, 45)
print('#'*50)
example_method(20, 40, ('Ranga', 'India', 1991))
print('#'*50)
example_method('Hello', 'World', 'This', 'is', 'Python')
print('#'*50)
example_method('Hello', 'World', 'This', 'is', 'Python', key1='A', key2='B')
print('#'*50)

# Returning multiple values in Python
def method():
    return 1, 10.5, 'string'

print('Returned values from method ', method())
print('#'*50)

# Name Tuple
Point = namedtuple('Point', ['x','y'])
point1 = Point(1, 2)

ThreeDPoint = namedtuple('ThreeDPoint', ['x', 'y', 'z'])
point2 = ThreeDPoint(1,2,3)

print('point 1 = ', point1)
print('point 2 = ', point2)

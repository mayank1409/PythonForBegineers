def example_method(mandatory_parameter, default_parameter='Default Parameter', *args, **kwargs):
    print(f'mandatory_parameter = {mandatory_parameter} and type = {type(mandatory_parameter)}')
    print(f'default_parameter = {default_parameter} and type = {type(default_parameter)}')
    print(f'args = {args} and type = {type(args)}')
    print(f'kwargs = {kwargs} and type = {type(kwargs)}')


list = [2,4,6,1,3,5]

example_method(list[0], list[1], list[2])
print('#'*50)

example_method(*list)
print('#'*50)

dict_ex = {'a':1, 'b':2}
example_method(*list, **dict_ex)

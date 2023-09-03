squares = [i*i for i in range(1, 11)]
print('squares of 1 to 10 ', squares)

square_set = {i*i for i in range(1, 11)}
print('squares of 1 to 10 ', square_set)

squares_dict = {i:i*i for i in range(1, 11)}
print('squares of dict of 1 to 10 ', squares_dict)

print(type([]))
print(type({}))
print(type(set()))

print(type({1}))
print(type({'A': 1}))

print(type(()))
numbers = [1,2,3,3,2,1]
numbers_set = set(numbers)
print('Set ', numbers_set)

numbers_set.add(0)
print('Set after add 0', numbers_set)

print('Is 1 in Set ', 1 in numbers_set)

print('Min in the set ', min(numbers_set))
print('Max in the set ', max(numbers_set))

# Set Operations

numbers_1_5_set = set(range(1,6))
print('Numbers from 1 to 5 ', numbers_1_5_set)

numbers_3_9_set = set(range(3,10))
print('Numbers from 3 to 9 ', numbers_3_9_set)

numbers_1_9_set = numbers_1_5_set | numbers_3_9_set
print('Union ', numbers_1_9_set)

numbers_3_5_set = numbers_1_5_set & numbers_3_9_set
print('Intersection ', numbers_3_5_set)

numbers_set_diff = numbers_1_5_set - numbers_3_5_set
print('Diff ', numbers_set_diff)

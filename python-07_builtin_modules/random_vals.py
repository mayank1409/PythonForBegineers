import random

print('Random Number ',random.random())
print('Random Number between 1 and 10 ', random.randint(1, 10))
print('Random Odd Number between 1 and 25 ', random.randrange(1, 25, 2))
print('Random Even Number between 1 and 25 ', random.randrange(2, 25, 2))

list = [2,7,4,9]
print('list = ', list)
print('Random from list = ', random.choice(list))
print('2 Random values from list ', random.sample(list, 2))

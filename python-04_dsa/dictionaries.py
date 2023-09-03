occurences = dict(a = 5, b = 6, c = 7)
print('Dict ', occurences)

print(type(occurences))
occurences['d'] = 15
occurences['d'] = 10

print(occurences.get('d')) # Type Safe Way of retrieving from dict
print(occurences.get('e', 11))

print('Keys in Dict ', occurences.keys())
print('Values in Dict ', occurences.values())

for (key, item) in occurences.items():
    print(f'{key} :: {item}', end=' ')
print()

del occurences['a']
print('Dict after del a', occurences)

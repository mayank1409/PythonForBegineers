def create_ranga():
    return 'Ranga','India',1984

ranga = create_ranga()
print(ranga)
print(type(ranga))
print(len(ranga))

x, y = 10, 20
print(f'before swap: x = {x}, y = {y}')
x, y = y, x
print(f'after swap: x = {x}, y = {y}')
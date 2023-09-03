i = 0

while i < 11:
    print(f'{i}')
    i += 1

def squares_of_numbers_upto(n):
    i = 1
    while i*i < n:
        print(f'{i}x{i} = {i*i}', end=' ')
        i += 1


squares_of_numbers_upto(100)
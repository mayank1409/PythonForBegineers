def print_cubes_of_positive_number():
    while True:
        i = int(input("Enter a number: (-ve to exit) "))
        if i < 0:
            break            
        print(f'{i} x {i} x {i} = {i*i*i}')
        b=True
    print('Thank You! Have Fun')


print_cubes_of_positive_number()
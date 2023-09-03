x = 5
if x > 3:
    print(f'{x} is grater than 3')

x = 1
if x > 3 and x < 6:
    print(f'{x} is between 3 and 6')
else:
    print(f'{x} is NOT between 3 and 6')

number = 6
isEven = True if number%2==0 else False

print(f'{number} is Even? {isEven}')

x = input("Enter a number")
x = int(x)

if x == 1:
    print(f'{x} is 1')
elif x == 2:
    print(f'{x} is 2')
else:
    print(f'{x} is neither 1 or 2')
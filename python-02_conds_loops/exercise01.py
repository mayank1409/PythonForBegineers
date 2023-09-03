def print_menu():
    print("Operations Available are: ")
    print("1 - Add")
    print("2 - Substract")
    print("3 - Multiply")
    print("4 - Divide")
    choice = input("Enter Your choice: ")
    choice = int(choice)
    if choice >= 1  and choice <= 4:
        print('You entered ', choice)
        calculate(choice)
    else :
        print("Invalid Choice")
    

def calculate(choice):
    number1 = input("Enter number1: ")
    number2 = input("Enter number2: ")

    number1 = int(number1)
    number2 = int(number2)

    if choice == 1:
        print(f'{number1} + {number2} = ', number1 + number2)
    elif choice == 2:
        print(f'{number1} - {number2} = ', number1 - number2)
    elif choice == 3:
        print(f'{number1} x {number2} = ', number1 * number2)
    elif choice == 4:
        print(f'{number1} / {number2} = ', number1 / number2)

print_menu()

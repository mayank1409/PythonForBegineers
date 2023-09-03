def print_squares_upto_n(n):
    for i in range(1, n+1):
        print(i*i)


def print_squares_of_evens_upto_n(n) :
    for i in range(2, n+1, 2) :
        print(i*i)


def print_numbers_in_reverse(n):
    for i in range(n,0,-1):
        print(i)


def sum_of_two_numbers(num1, num2):
    sum=num1+num2
    return sum


print_squares_upto_n(10)
print("Done")
print_squares_of_evens_upto_n(10)
print("Done")
print_numbers_in_reverse(10)
print("Done")
sum = sum_of_two_numbers(10, 20)
print(f"sum of 10 and 20 = {sum}")
print("Done")

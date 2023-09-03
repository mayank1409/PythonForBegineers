def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if (n % i == 0):
            return False
    return True


def sum_upto_n(n):
    sum = 0
    for i in range (1, n+1):
        sum += i
    return sum


def sum_of_divisors(n):
    sum = 0
    for i in range(2, n):
        if n % i == 0:
            sum = sum + i
    return sum

def print_number_triangle(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()


print(is_prime(13))
print(sum_upto_n(10))
print(sum_of_divisors(10))
print_number_triangle(5)

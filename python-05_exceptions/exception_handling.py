try:
    i=0
    x=10/i
except ZeroDivisionError as error:
    print(error)
    x = 0.0
else:
    print('else will execute only if exception will not happened')
finally:
    print('finally')
print(x)

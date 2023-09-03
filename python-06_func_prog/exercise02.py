from functools import reduce

months = [('Jan', 31), ('Feb', 28), ('Mar', 31)]
print('Months given ', months)
print('Sum of days for given months ', reduce(lambda x,y:x+y, list(map(lambda month:month[1], months))))
print('Name of month with least days ', reduce(lambda x,y:x if x[1] < y[1] else y, months)[0])

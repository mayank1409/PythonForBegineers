from functools import reduce

nums = [3, 7, 8, 15, 24, 35, 46]
print('Nums ', nums)

even_nums_squared_sum = reduce(lambda x,y: x+y, list(map(lambda num:num**2,list(filter(lambda num:num%2 == 0, nums)))))
print('Even nums squared sum ', even_nums_squared_sum)

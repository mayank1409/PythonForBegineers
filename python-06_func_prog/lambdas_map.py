words = ['Apple', 'Ant', 'Bat']
print('Words ', words)

words_upper = list(map(lambda word:word.upper(), words))
print('words upper case ', words_upper)

words_len = list(map(lambda word:len(word), words))
print('words len ', words_len)

nums = [1, 5, 2, 9]
print('Numbers ', nums)

nums_squared = list(map(lambda num:num**2, nums))
print('Nums squared ', nums_squared)

squares_1_10 = list(map(lambda num:num**2, range(1, 11)))
print('squares 1 to 10 ', squares_1_10)

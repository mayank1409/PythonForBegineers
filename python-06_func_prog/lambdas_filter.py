nums = [1, 89, 35, 54]

odds = list(filter(lambda num:num%2==1,nums))
print('odds ', odds)

evens = list(filter(lambda num:num%2==0,nums))
print('evens ', evens)

words = ['Apple', 'Banana', 'Bat', 'Ant']
print('Words ', words)

words_ends_with_at = list(filter(lambda word:word.endswith('at'), words))
print('words ends with \'at\'', words_ends_with_at)

words_with_len_3 = list(filter(lambda word:len(word)==3, words))
print('words with len 3 ', words_with_len_3)

words_starts_with_a = list(filter(lambda word:word.startswith('A'), words))
print('words starts with \'A\'', words_starts_with_a)

numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

numbers_len_four = []

for number in numbers:
    if len(number) == 4:
        numbers_len_four.append(number)

print('Numbers List: ', numbers)
print('Numbers with Length four: ', numbers_len_four)

numbers_len_four = [number for number in numbers if len(number) == 4]
print('Numbers with length four with List comprehension: ', numbers_len_four)

values = [3, 6, 1, 9, 4, 15, 6, 3]
value_even = [value for value in values if value % 2 == 0]
value_odd = [value for value in values if value % 2 == 1]

print('Values ', values)
print('Even Values ', value_even)
print('Odd values ', value_odd)

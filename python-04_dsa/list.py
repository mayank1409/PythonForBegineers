marks = [23, 67, 43]
marks.append(90)
marks.insert(2, 60)

print('List: ', marks)

print('Traversing through marks: ')
for mark in marks :
    print(mark)


print('Sum of marks: ', sum(marks))
print('Max of marks: ', max(marks))
print('Is 60 in Marks: ', 60 in marks)
print('Is 61 in marks: ', 61 in marks)
print('Length of marks ', len(marks))
print('Index of 90 in marks: ', marks.index(90))


animals = ['Cat', 'Dog', 'Elephant']
animals.append('Fish')
animals.remove('Dog')
del animals[2]
print('Animals List: ', animals)
print('Animals Length ', len(animals))
animals.extend(['Fish', 'Giraffe', 'Horse'])
animals.append('Fish')
print('Animals List: ', animals)

animals += ['Jackle', 'Kangaroo']
print('Animals List Now : ', animals)
animals = animals + ['Lion', 'Monkey']
print('Animals List after adding Lion and Monkey: ', animals)

# Python List Slicing 

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2])
print('list of numbers: ', numbers)
print('list slicing in action: ', numbers[2:6])
print('list slicing from 0 to 3: ', numbers[:3])
print('list slicing from 2 and every 2nd element: ', numbers[2::2])
print('list slicing from 0 and every 3nd element: ', numbers[::3])
print('list slicing from 1 to 8 and every 2nd element ', numbers[1:8:2])
print('list slicing from reverse order and every 3rd element: ', numbers[::-3])
del numbers[5:7]
print('deleting using list slicing, deleting 5th and 6th value ', numbers)
numbers[5:7] = ['Seven', 'Eight']
print('updating list using slicing, numbers ', numbers)


# Sort and Reverse operations on Python List

numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
numbers.reverse()
print('Numbers list: ', numbers)

print('Reinitlizing numbers: ')
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
for number in reversed(numbers):
    print(number, end=' ')
print()

print('Sorting numbers')
numbers.sort()
print(numbers)

print('Reinitlizing numbers and printing using sorted: ')
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
for number in sorted(numbers):
    print(number, end=' ')
print()

print('Numbers List: ', numbers)
for number in sorted(numbers, key=len):
    print(number, end=' ')
print()

for number in sorted(numbers, key=len, reverse=True):
    print(number, end=' ')
print()

numbers.sort(key=len)
print('Numbers ', numbers)

numbers.sort(key=len, reverse=True)
print('Numbers ', numbers)

# List as Stack and Queue

numbers = []
numbers.append(10)
numbers.append(20)
numbers.append(30)

numbers.pop()
print('Numbers: ', numbers)

numbers.append(40)
numbers.append(50)

numbers.pop()
print('Numbers: ', numbers)

numbers = []

numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)

numbers.pop(0)
print('Numbers: ', numbers)
numbers.pop(0)
print('Numbers: ', numbers)
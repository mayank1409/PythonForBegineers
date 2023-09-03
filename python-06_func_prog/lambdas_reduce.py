from functools import reduce

nums = [3,15,12,10]
print('nums ', nums)

print('Sum of nums ', reduce(lambda x,y: x+y, nums))
print('Product of nums ', reduce(lambda x,y: x*y, nums))
print('Max of nums ', reduce(lambda x,y:max(x,y), nums))
print('Min of nums ', reduce(lambda x,y:min(x,y), nums))

words = ['Apple', 'Ant', 'Banana']
print('Words ', words)
print('Word with max len ', reduce(lambda x,y:x if len(x) > len(y) else y, words))

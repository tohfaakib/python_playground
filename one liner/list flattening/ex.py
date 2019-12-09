import itertools

a_list = [[1, 2], [3, 4], [5, 6]]
print(list(itertools.chain.from_iterable(a_list)))

# or

print(list(itertools.chain(*a_list)))


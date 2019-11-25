list_with_dup = ['a', 'b', 'c', 'b', 'd', 'e', 'c']

lists = set([x for x in list_with_dup if list_with_dup.count(x) > 1])

print(lists)
print(sorted(list(set(list_with_dup))))


mother_set = set(['a', 'b', 'c', 'd'])
input_set = set(['z', 'y', 'b'])

# intersection
print('intersection: ')
output = mother_set.intersection(input_set)
print(output)

# Union
print('Union: ')
output = mother_set.union(input_set)
print(output)

# Difference
print('Difference: ')
output = mother_set.difference(input_set)
print(output)
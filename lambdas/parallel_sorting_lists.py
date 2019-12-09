# for py2

list1 = [5, 7, 4, 1, 2, 3, 4]
list2 = ['z', 'v', 'y', 'a', 'b', 'c', 'd']

zipped = zip(list1, list2)

zipped.sort()

list1, list2 = map(lambda t: list(t), zip(*zipped))

print(list1)
print(list2)



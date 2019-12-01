def add_to(num, target=[]):
    target.append(num)
    return target


print(add_to(1))
# output: [1]
print(add_to(2))
# output: [1, 2]
print(add_to(3))
# output: [1, 2, 3]


def add_to_2(num, target=None):
    if target is None:
        target = []
    target.append(num)
    return target


print(add_to_2(1))
# output: [1]
print(add_to_2(2))
# output: [2]
print(add_to_2(3))
# output: [3]

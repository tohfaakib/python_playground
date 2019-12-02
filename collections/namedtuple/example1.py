from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')

smudge = Animal(name='smudge', age='idk', type='cat')

print(smudge)
print(smudge[2])

print(smudge.name)
print(smudge.age)
print(smudge.type)

# namedtuple can be converted to dictionary

print(smudge._asdict())

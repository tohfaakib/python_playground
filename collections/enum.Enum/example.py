from collections import namedtuple
from enum import Enum


class Species(Enum):
    cat = 1
    dog = 2
    horse = 3
    aardvark = 4
    butterfly = 5
    owl = 6
    platypus = 7
    dragon = 8
    unicorn = 9
    # The list goes on and on...
    # But we don't really care about age, so we can use an alias.
    kitten = 1
    puppy = 2


Animal = namedtuple('Animal', 'name age type')
perry = Animal(name='perry', age=31, type=Species.cat)
smudge = Animal(name='smudge', age=31, type=Species.kitten)

print(perry.type == smudge.type)

print(Species(1))
print(Species['cat'])
print(Species.cat)

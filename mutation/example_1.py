foo = ['hi']

print(foo)
#  ['hi']

bar = foo

bar += ['bye']

print(foo)
#  ['hi', 'bye']

foo += ['hello']
print(bar)
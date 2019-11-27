# this method is avoided

fat = True

fitness = ('fat', 'skinny')[fat]
print(fitness)


# there are many reason f avoiding tupled ternary operations.
# example:

print('conditonal(if-else) ternary operations: ')
print(5 if True else 5/0)

print('tupled ternary operations: ')
try:
    print((5/0, 2)[True])
except Exception as e:
    print("Error:", e)

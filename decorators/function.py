def hi(name="Nishan"):
    return 'Hi ' + name


print("hi(): ", hi())

greet = hi

print("greet(): ", greet())

del hi

try:
    print("hi(): ", hi())
except Exception as e:
    print('hi() error:', e, '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


print("greet(): ", greet())

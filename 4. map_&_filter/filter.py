num_list = range(-5, 5)

print(num_list)

less_than_zero = list(filter(lambda x: x < 0, num_list))
print(less_than_zero)

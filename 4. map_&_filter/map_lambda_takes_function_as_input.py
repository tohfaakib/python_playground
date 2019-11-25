def squre(x):
    return x ** 2

def add(x):
    return x + x

func_list = [add, squre]
for i in range(10000000):
    value = list(map(lambda x: x(i), func_list))
    print(value)

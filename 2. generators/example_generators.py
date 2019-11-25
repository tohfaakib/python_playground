def generator_func():
    for i in range(10):
        yield i


for item in generator_func():
    print(item)

def gen_func():
    for i in range(3):
        yield i


gen = gen_func()
print(next(gen))
print(next(gen))
print(next(gen))


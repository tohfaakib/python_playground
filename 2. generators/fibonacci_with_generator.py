def fibonacci_generator(limit):
    a = 0
    b = 1
    yield a
    yield b
    for i in range(limit):
        a = a + b
        yield a
        temp = b
        b = a
        a = temp


for num in fibonacci_generator(1000):
    print(num)

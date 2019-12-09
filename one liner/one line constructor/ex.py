class A(object):
    def __init__(self, a, b, c, d, e, f):
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})


a = A(1, 2, 3, 4, 5, 6)

print(a.__dict__)

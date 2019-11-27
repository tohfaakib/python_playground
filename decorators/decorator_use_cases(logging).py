from functools import wraps


def get_log(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} has been called')
        return func(*args, **kwargs)

    return wrapper


@get_log
def addition(x):
    return x + x


print(addition(2))

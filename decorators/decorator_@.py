from functools import wraps


def new_decorator(func):

    @wraps(func)
    def wrapper():
        print("before calling func()")

        func()

        print("after calling func()")

    return wrapper


@new_decorator
def the_great_ugly_func():
    print("you ugly *****, you need be decorated!")


print("Function name:", the_great_ugly_func.__name__)

the_great_ugly_func()

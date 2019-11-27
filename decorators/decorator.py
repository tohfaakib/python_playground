from functools import wraps

def new_decorator(func):

    @wraps(func)
    def wrapper():
        print("before calling func()")

        func()

        print("after calling func()")

    return wrapper


def the_great_ugly_func():
    print("you ugly *****, you need be decorated!")


the_great_ugly_func()

the_great_ugly_func = new_decorator(the_great_ugly_func)

print("Function name:", the_great_ugly_func.__name__)

the_great_ugly_func()

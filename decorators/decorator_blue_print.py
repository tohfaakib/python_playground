from functools import wraps


def the_decorator(func):

    @wraps(func)
    def the_wrapper(*args, **kwargs):
        if not can_run:
            return "Function cannot run!!"
        else:
            return func(*args, **kwargs)

    return the_wrapper


@the_decorator
def the_ugly_func():
    return "Function is running!"


can_run = True
print(the_ugly_func())

can_run = False
print(the_ugly_func())

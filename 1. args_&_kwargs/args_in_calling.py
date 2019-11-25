def args_calling_func(arg1, arg2, arg3):
    print(arg1)
    print(arg2)
    print(arg3)


args = ('a', 'b', 'c')
args_calling_func(*args)

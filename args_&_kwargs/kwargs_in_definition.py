def kwargs_definition(normal, **kwargs):  # here kwargs is a convention. anything can be written here instead of
    # kwargs, like,
    # **vars, **a, **something! here the only important thing is the double asterisk(**)! kwargs is used to pass
    # keyworded arguments!
    print("Normal parameter:", normal)

    print(type(kwargs))  # its a dictionary type argument
    print(kwargs["name"])
    print(kwargs["age"])

    for key, value in kwargs.items():
        print('{} = {}'.format(key, value))


kwargs_definition("Hi", name="Nishan", age="80")


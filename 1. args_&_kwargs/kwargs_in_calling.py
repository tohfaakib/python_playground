def kwargs_calling_func(name, age):
    print(name)
    print(age)


kwargs = {'name': 'nishan', 'age': 80}
kwargs_calling_func(**kwargs)

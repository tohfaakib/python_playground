def args_definition(normal, *args):  # here args is a convention. anything can be written here instead of args, like,
    # *vars, *a, *something! here the only important thing is the single asterisk(*)! and it is used to pass
    # non-keyworded  variable(multiple or single) variable argument.
    print("Normal parameter:", normal)

    print("Args:", args)  # args is a tuple with the values passed in it!


args_definition("normal value", "value 1 in args", "value 2 in args", "value 3 in args", "value 4 in args")

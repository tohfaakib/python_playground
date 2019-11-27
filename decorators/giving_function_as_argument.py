def hi(name="Tohfa Akib"):
    return "Hello, {}".format(name)

def before_hi(func):
    print("You cannot just say hi, atleast offer some food!")
    print(func())


before_hi(hi)

def hi(name="Nishan"):
    def greet(n):
        return n + " you are inside greet function!!!!"

    def welcome(n):
        return n + " you are inside welcome function!!!!"

    if name == "Nishan":
        return greet
    else:
        return welcome


# f = hi()()
# print(f)

# f = hi()
# print(f())

f = hi("Tohfa")
print(f('Nishan'))

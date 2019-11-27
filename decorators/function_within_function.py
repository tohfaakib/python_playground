def hi():
    print("inside hi() function!")

    def greet():
        print("inside greet() function!")

    def welcome():
        print("inside welcome() function!")

    print(greet())
    print(welcome())
    print("back to hi() function")


hi()

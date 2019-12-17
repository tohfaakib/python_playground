def grep(pattern):
    print("Searching for pattern: ", pattern)

    while True:
        line = (yield)
        if pattern in line:
            print(line)


search = grep('tin')

next(search)

search.send("How are you tintin?")
search.send("You like tantin?")
search.send("I don't know!")
search.send("You like coroutine?")



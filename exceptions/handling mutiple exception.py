try:
    file = open("file.txt", 'rb')
except (IOError, EOFError) as e:
    print(f"Error occurred: {e.args[-1]}")

# =============================================

try:
    file = open('test.txt', 'rb')
except EOFError as e:
    print("An EOF error occurred.")
    raise e
except IOError as e:
    print("An error occurred.")
    raise e

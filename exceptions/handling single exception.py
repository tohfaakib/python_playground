try:
    file = open('file.txt', 'rb')
except IOError as e:
    print("An IOError occurd: {}".format(e.args[-1]))


#  =================================================================

try:
    file = open('test.txt', 'rb')
except Exception:
    # Some logging if you want
    raise

# ================================ Normal Case ===========================


def addition(val1, val2):
    return val1 + val2


result = addition(10, 20)
print(result)


# ================================= Global ==================================


def addition_g(val1, val2):
    global result_g
    result_g = val1 + val2


addition_g(30, 40)
print(result_g)

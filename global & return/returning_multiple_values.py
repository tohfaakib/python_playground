def division(num1, num2):
    result = num1 // num2
    remainder = num1 % num2

    # result_in_tuple = (result, remainder)
    # return result_in_tuple
    return result, remainder


result, remainder = division(11, 3)

print(result)
print(remainder)

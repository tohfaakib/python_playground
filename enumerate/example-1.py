a_list = [1,2,3,4,5,6,7,8,9]

for counter, item in enumerate(a_list):
    print(f"{counter} - {item}")

print("===========================================================")


for counter, item in enumerate(a_list, 1):
    print(f"{counter} - {item}")


print("===========================================================")


my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1))

print(counter_list)

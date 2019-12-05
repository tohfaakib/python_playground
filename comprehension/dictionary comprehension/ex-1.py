my_dict = {
    'a': 'hello',
    'b': 'apple',
    'c': 'sky',
    'd': 'bmw'
}

new_dict = {value: key for key, value in my_dict.items()}

print(new_dict)

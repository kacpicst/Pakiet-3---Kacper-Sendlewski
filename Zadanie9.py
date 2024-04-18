def zip_with_index(input_list):
    return [(item, index) for index, item in enumerate(input_list)]

original_list = ['a', 'b', 'c', 'd']
result = zip_with_index(original_list)
print(result)

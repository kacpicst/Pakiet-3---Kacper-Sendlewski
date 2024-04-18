def count_unique_elements(input_list):
    return len(set(input_list))

original_list = [1, 2, 3, 1, 2, 3, 4, 5]
result = count_unique_elements(original_list)
print(result)
def split_list(input_list, chunk_size):
    return [input_list[i:i+chunk_size] for i in range(0, len(input_list), chunk_size)]

original_list = [1, 2, 3, 4, 5, 6, 7, 8]
result = split_list(original_list, 3)
print(result) 
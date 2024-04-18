def find_max_min_diff(input_list):
    if not input_list:
        return None
    max_val = max(input_list)
    min_val = min(input_list)
    return max_val - min_val

numbers = [1, 9, 3, 7, 5]
result = find_max_min_diff(numbers)
print(result)

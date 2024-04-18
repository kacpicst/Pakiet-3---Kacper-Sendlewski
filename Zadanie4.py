def remove_duplicates(input_list):
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

original_list = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(original_list)
print(result)

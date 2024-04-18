def recursive_sum(input_list):
    total = 0
    for element in input_list:
        if isinstance(element, list):
            total += recursive_sum(element)
        else:
            total += element
    return total

nested_list = [1, 2, [3, 4], [5, [6, 7]], 8]
result = recursive_sum(nested_list)
print(result)

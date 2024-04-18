def cumulative_sum(input_list):
    cumulative = []
    total = 0
    for item in input_list:
        total += item
        cumulative.append(total)
    return cumulative

original_list = [1, 2, 3, 4, 5]
result = cumulative_sum(original_list)
print(result)

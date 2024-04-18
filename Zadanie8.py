def partition_list(input_list, condition):
    true_list = [x for x in input_list if condition(x)]
    false_list = [x for x in input_list if not condition(x)]
    return true_list, false_list

original_list = [1, 2, 3, 4, 5, 6]
result_true, result_false = partition_list(original_list, lambda x: x % 2 == 0)
print(result_true)
print(result_false)

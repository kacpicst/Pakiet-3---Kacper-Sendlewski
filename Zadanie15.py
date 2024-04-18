def custom_sort(input_list, key_function):
    return sorted(input_list, key=key_function)

original_list = ['Suzuki', 'Honda', 'Audi', 'BMW', 'RollsRoyce']
result = custom_sort(original_list, key_function=lambda x: len(x))
print(result)

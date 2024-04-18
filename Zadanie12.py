def rotate_list(input_list, steps):
    steps = steps % len(input_list)
    return input_list[-steps:] + input_list[:-steps]

original_list = [1, 2, 3, 4, 5]
rotated_list = rotate_list(original_list, 2)
print(rotated_list)

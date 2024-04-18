def sum_of_squares_of_odds(input_list):
    return sum(x**2 for x in input_list if x % 2 != 0)

numbers = [1, 2, 3, 4, 5]
result = sum_of_squares_of_odds(numbers)
print(result)

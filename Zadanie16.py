def remove_whitespace(string_list):
    return [string.replace(" ", "") for string in string_list]

original_list = ["zielone jabłko", "czarny samochód", "żółta pszczoła", "coś za coś"]
result = remove_whitespace(original_list)
print(result) 

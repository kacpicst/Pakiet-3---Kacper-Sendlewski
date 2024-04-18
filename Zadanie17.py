def capitalize_all_words(string_list):
    return [word.capitalize() for word in string_list]

original_list = ["cześć wam", "zadania są okej", "warto je robić"]
result = capitalize_all_words(original_list)
print(result)

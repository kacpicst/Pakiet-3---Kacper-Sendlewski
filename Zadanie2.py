def filter_long_words(string_list):
    average_length = sum(len(word) for word in string_list) / len(string_list)
    
    filtered_list = [word for word in string_list if len(word) > average_length]
    
    return filtered_list

words_list = ["jabłko", "banan", "mandarynka", "truskawka", "kiwi", "arbuz"]
filtered_words = filter_long_words(words_list)
print(filtered_words)

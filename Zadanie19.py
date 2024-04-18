def check_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

string1 = "arbuz"
string2 = "burza"
result = check_anagrams(string1, string2)
print(result) 

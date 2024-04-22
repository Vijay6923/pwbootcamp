def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    if len(str1) != len(str2):
        return False
    char_count_str1 = {}
    char_count_str2 = {}
    for char in str1:
        char_count_str1[char] = char_count_str1.get(char, 0) + 1

    for char in str2:
        char_count_str2[char] = char_count_str2.get(char, 0) + 1

    
    return char_count_str1 == char_count_str2


string1 = "listen"
string2 = "silent"
if are_anagrams(string1, string2):
    print(f"'{string1}' and '{string2}' are anagrams.")
else:
    print(f"'{string1}' and '{string2}' are not anagrams.")

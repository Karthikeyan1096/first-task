from collections import Counter

def count_unique_characters(s):
    char_counter = Counter(s)
    return len(char_counter)

input_string =  input("Enter a string: ")
print(count_unique_characters(input_string))

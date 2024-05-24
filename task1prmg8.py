def count_words(input_string):
    words = input_string.split()
    return len(words)
user_input = input("Enter a string: ")
word_count = count_words(user_input)
print(f"Number of words in the input string: {word_count}")

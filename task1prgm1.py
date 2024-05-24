input_string = input('Enter the string: ')
count = 0
String = input_string.lower()
for vowel in String:
    if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u':
        count += 1
if count == 0:
    print('No vowels found')
else:
    print('Total number of vowels in the string: ' + str(count))

def find_longest_common_substring(string1, string2):
    m, n = len(string1), len(string2)
    LCSuff = [[0] * (n + 1) for _ in range(m + 1)]
    result = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:
                LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1
                if LCSuff[i][j] > result:
                    result = LCSuff[i][j]
                    longest_substring_i1, longest_substring_i2 = i, j
            else:
                LCSuff[i][j] = 0
    longest_common_substring = string1[longest_substring_i1 - result : longest_substring_i1]
    return longest_common_substring

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
print("Longest common substring:", find_longest_common_substring(string1, string2))

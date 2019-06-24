def longest_substring(string):
    substrings = []
    letter_index = {}
    max_index_of_string = len(string) - 1
    for index, letter in enumerate(string):
        if letter_index.get(letter) is not None:
            previous_index = letter_index[letter]
            substrings.append(string[previous_index:index])
            letter_index[letter] = index
        else:
            letter_index[letter] = index

    # substrings for "pwwkew" are ["w", "wke"] which is incorrect
    if not substrings:
        substrings.append(string)
    return max(len(letter) for letter in substrings)

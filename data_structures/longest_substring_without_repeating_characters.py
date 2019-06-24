def longest_substring(string):
    substrings = []
    letter_index = {}
    for index, letter in enumerate(string):
        if letter_index.get(letter):
            previous_index = letter_index[letter]
            substrings.append(string[previous_index:index])
            letter_index[letter] = index
        else:
            letter_index[letter] = index
    return max(len(letter) for letter in substrings)

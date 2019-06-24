def longest_substring(string):
    substrings = []
    letter_index = {}
    for index, letter in enumerate(string):
        import pdb
        pdb.set_trace()
        if letter_index.get(letter) is not None:
            previous_index = letter_index[letter]
            substrings.append(string[previous_index:index])
            letter_index[letter] = index
        else:
            letter_index[letter] = index
    if not substrings: # this solves the " " problem but not "aab", "ab" substring never gets added
        substrings.append(string)
    return max(len(letter) for letter in substrings)

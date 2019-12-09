def longest_substring(string):
    substrings = ''
    longest_substring = ''
    if not string:
        return 0
    for letter in string:
        if letter in substrings:
            letter_location = substrings.index(letter)
            if letter_location == 0:
                substrings = substrings[1:]
                substrings = substrings + letter
            else:
                if len(longest_substring) < len(substrings):
                    longest_substring = substrings
                substrings = substrings[letter_location+1:]
                substrings = substrings + letter
        else:
            substrings = substrings + letter

    if len(longest_substring) < len(substrings):
        longest_substring = substrings

    return len(longest_substring)

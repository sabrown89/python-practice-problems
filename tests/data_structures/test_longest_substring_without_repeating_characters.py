import pytest
from practice_problems.data_structures import longest_substring_without_repeating_characters as lswrc


@pytest.mark.parametrize(
    "test_input, expected", [
    #("abcabcbb", 3),
    #(" ", 1),
    #("aa", 1),
    ("aab", 2)])
    #("bbbbb", 1),
    #("pwwkew", 3)])
def test_longest_substring(test_input, expected):
    assert lswrc.longest_substring(test_input) == expected

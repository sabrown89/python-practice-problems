from practice_problems.problems import anagrams

a = 'abc'
b = 'cde'

def test_number_of_swaps():
    assert anagrams.number_of_swaps(a,b) == 4

from app import amazing_strings

unamazing_list = ['baaaaaaaaaccccbaabaaccc', 'bab', 'bba']
ams = amazing_strings.AmazingStrings(unamazing_list)

def test_count_of_repeating_letters():
    string_1 = 'baaaaaaaaaccccbaabaaccc'
    assert ams.count_of_repeating_letters(string_1) == [8,3,1,1,2]
    string_2 = 'bab'
    assert ams.count_of_repeating_letters(string_2) == []
    string_3 = 'bba'
    assert ams.count_of_repeating_letters(string_3) == [1]

def test_count_replacements_needed():
    string_1 = 'baaaaaaaaaccccbaabaaccc'
    assert ams.count_replacements_needed(string_1) == 9
    string_2 = 'bab'
    assert ams.count_replacements_needed(string_2) == 0
    string_3 = 'bba'
    assert ams.count_replacements_needed(string_3) == 1

def test_amazing_string_count():
    assert ams.amazing_string_count() == [9,0,1]

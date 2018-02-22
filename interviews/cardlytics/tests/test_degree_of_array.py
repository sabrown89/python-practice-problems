from app import degree_of_array

array = [1,2,2,3,1]
doa = degree_of_array.DegreeOfArray(array)

def test_find_degree():
    assert doa.find_degree() == 2

def test_find_ints_with_degree():
    assert doa.find_ints_with_degree() == [1,2]

def test_find_substrings_for():
    item = 2
    assert doa.find_substrings_for(item) == [2,2]
    item = 1
    assert doa.find_substrings_for(item) == [1,2,2,3,1]

def test_find_smallest_substring_of_degree():
    assert doa.find_smallest_substring_of_degree() == 2


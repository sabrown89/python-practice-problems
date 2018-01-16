from practice_problems.problems import bubble_sort


def test_sort_list():
    unsorted_list = [4,1,6,2,3,7,5]
    s = bubble_sort.BubbleSort(unsorted_list)
    s.sort_list()
    assert s.unsorted_list == [1,2,3,4,5,6,7]

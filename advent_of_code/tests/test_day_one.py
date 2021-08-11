from advent_of_code.day_one import day_one, day_one_part_two

def test_day_one():
    assert day_one([1721, 979, 366, 299, 675, 1456]) == 514579

def test_day_one_part_two():
    assert day_one_part_two([1721, 979, 366, 299, 675, 1456]) == 241861950

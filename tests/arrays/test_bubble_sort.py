from practice_problems.arrays.left_rotation import left_rotation


def test_left_rotation_four():
    array = [1, 2, 3, 4, 5]
    rotations = 4
    assert left_rotation(array, rotations) == [5, 1, 2, 3, 4]

def test_left_rotation_two():
    array = [1, 2, 3, 4, 5]
    rotations = 2
    assert left_rotation(array, rotations) == [3, 4, 5, 1, 2]

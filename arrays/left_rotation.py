"""
A left rotation operation on an array shifts each of the array's elements 1 unit tot he left. For example, if 2 left rotations are performed on array [1, 2, 3, 4, 5], then the array would become [3, 4, 5, 1, 2].

Given an array of n integers and a number, perform the number of rotations on the array. Return the updated array to be printed as a single line of space-separated integers.
"""
def left_rotation(array, rotations):
    for rotation in range(rotations):
        first_element = array.pop(0)
        array.append(first_element)

    return array

list_to_search = [1,4,9,10,11,15,20,55]
target_value = 19


def binary_search(list_passed_in, target_value):
    if len(list_passed_in) < 2:
        return False
    median = int(len(list_passed_in)/2)
    if list_passed_in[median] == target_value:
        return True
    if list_passed_in[median] < target_value:
        return binary_search(list_passed_in[median:], target_value)
    return binary_search(list_passed_in[:median], target_value)

result = binary_search(list_to_search, target_value)
print(result)

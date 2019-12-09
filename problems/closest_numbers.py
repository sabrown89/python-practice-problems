#list_b = [4, 1, 2, 10, 5, 20]
#list_a = [-1, 3, 8, 2, 9, 5]
#target = 24
#
#def closest_pair(list_a, list_b, target):
#    temp_closest_sum = None
#    closest_pair = []
#    for number_a in list_a:
#        for number_b in list_b:
#            if not temp_closest_sum:
#                temp_closest_sum = abs((number_a + number_b) - target)
#                closest_pair = [number_a, number_b]
#                continue
#            temp_sum = number_a + number_b
#            if temp_closest_sum > abs(temp_sum - target):
#                temp_closest_sum = abs(temp_sum - target)
#                closest_pair = [number_a, number_b]
#    return closest_pair
## trying to find a match between the two to exactly the target and then going one off target, two off target
#
#
#print(closest_pair(list_a, list_b, target))

def some_function(bingo, list_b):
    try:
        list_b[bingo]
        bingo += 1
        some_function(bingo, list_b)
    except IndexError:
        pass
    finally:
        return bingo

list_b = [-1, 3, 8, 2, 9, 5]
response = some_function(1, list_b)
print('---->', response)

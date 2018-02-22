def array_left_rotation(n,k):
    for num in range(0,n):
        removed_int = k.pop(0)
        k.append(removed_int)
    return ' '.join(str(x) for x in k)

n = 3
k = [1,2,3,4,5]
print(array_left_rotation(n,k))

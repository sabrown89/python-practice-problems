previous_calculation = {}
#def fib(num):
#    if num <= 1:
#        return num
#    if previous_calculation.get(num):
#        print(num)
#        return previous_calculation[num]
#    else:
#        result = fib(num - 1) + fib(num-2)
#        previous_calculation[num] = result
#    return result

def fib(num):
    previous_calculation = {}
    for i in range(1, num + 1):
        if i == 1 or i == 2:
            previous_calculation[i] = 1
        else:
            result = previous_calculation[i - 1] + previous_calculation[i - 2]
            previous_calculation[i] = result
    return result

nterms = 10
#print("Fibonacci sequence: ")
#for i in range(nterms):
#    print(fib(i))
print(fib(6))

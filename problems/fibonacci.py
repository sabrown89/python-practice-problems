def fib(num):
    if num <= 1:
        return num
    return(fib(num - 1) + fib(num - 2))

nterms = 10
print("Fibonacci sequence: ")
for i in range(nterms):
    print(fib(i))

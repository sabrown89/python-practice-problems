def fib(N: int) -> int:
    if N == 0:
        return 0
    elif N == 1:
        return 1
    return fib(N - 1) + fib(N - 2)

print(fib(N=0))
print(fib(N=1))
print(fib(N=2))
print(fib(N=3))
print(fib(N=4))
print(fib(N=5))

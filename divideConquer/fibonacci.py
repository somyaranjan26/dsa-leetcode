# Fibonacci Sequence
    
# 1. Iterative
# def fib(n):   
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         a = 0
#         b = 1
#         for i in range(2, n + 1):
#             c = a + b
#             a = b
#             b = c
#         return c


# 2. Recursive
def fib(n):
    if n == 0:
        return 0
    elif n == 1:  
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
    
n = 4
result = fib(n+1)
print(f'Fibonacci of {n} is {result}')
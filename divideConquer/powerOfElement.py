def findPowerOfElement(a,n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    else:
        # Big Problem
        # ! Divide
        mid = n//2
        
        # ! Conquer
        b = findPowerOfElement(a, mid)
        
    # ! Combine
    result = b * b
    # ? check of Odd/Even
    if n % 2 == 0:
        return result
    else:
        return result * a
        

a = 2
n = 14
result = findPowerOfElement(a, n)
print(f'{a} ^ {n} = {result}')
#  Reverse Integer

# Input: x = 123
# Output: 321

# Input: x = -123
# Output: -321

# Input: x = 120
# Output: 21


import math

# Solution 1: Using in-built functions
# Time Complexity: O(n), because the time complexity of 
# the in-built functions str(), int(), and [::-1] is O(n)
# Space Complexity: O(n)
def reverse(x):
    # convert the integer to a string
    s = str(x)
    
    # check if the integer is negative
    if s[0] == '-':
        # reverse the string
        # ? [1:] means from the second character to the end
        # ? [::-1] means from the end to the beginning
        s = s[1:][::-1]
        
        # convert the string to an integer
        s = int(s)
        
        # check if the integer is within the range of 32-bit signed integer
        # ? ** is the exponentiation operator used to calculate the power of a number
        if s > (2**31)-1:
            return 0
        
        # return the negative integer
        return -s
    
    else:
        s = int(s[::-1])
        if s > (2**31)-1:
            return 0
        
        return s

    
# Solution 2: Using math
def reverse2(x):
    reverse = 0
    
    while x != 0:
        if x < 0:
            digit = x % -10
        
        
        digit = x % 10
        print(digit)
        
        reverse = reverse * 10 + digit
        print(reverse)
        
        # ? // is the floor division operator returns the integer part of the quotient
        x = x // 10
        print(x)
        
    if reverse > math.pow(2, 31) - 1 or reverse < -math.pow(2, 31):
        return 0
    
    return reverse


if __name__ == '__main__':
    x = 1238
    print(reverse2(x))
    
    # x = -1237
    # print(reverse2(x))
    
    # x = -120
    # print(reverse2(x))
    
    # x = 1534236469
    # print(reverse2(x))
    
    # x = -2147483648
    # print(reverse2(x))
# Roll Back Good Version (Binary Search)

# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
# You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version.
# You should minimize the number of calls to the API.

# Example:
# Given n = 5, and version = 4 is the first bad version.
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.

# Solution:

def isBadVersion(version):
    return True if version > 0 else False

# Recursive Approach
def helper(v, l, r):
    # ? calculate mid this way to avoid overflow
    m = l + (r - l) // 2
    
    # ? if l == r then we have reached the last element
    if l == r:
        return l
    
    # ? if l > r then we have crossed the last element
    if l > r:
        return -1
    
    # ? if v[m] is bad version and v[m-1] is not bad version then v[m] is the first bad version
    if isBadVersion(v[m]) == True:
        if isBadVersion(v[m - 1]) == False:
            return m
        else:
            return helper(v, l, m - 1)
    else:
        return helper(v, m + 1, r)

def badVersion(v):
    result = 0
    l = 0
    r = len(v) - 1
    
    # Brute Force Approach
    # for i in range(len(v)):
    #     if isBadVersion(v[i]) == True:
    #         result = i
    #         break
         

    # Binary Search Approach   
    # while l <= r:
    #     m = (r + l) // 2
        
    #     if isBadVersion(v[m]) == True:
    #         result = m
    #         r = m - 1
    #     else:
    #         l = m + 1
    
    # return result
    
    result = helper(v, l, r)
    return result


v = [0,0,0,1,1,1,1]
print(badVersion(v))
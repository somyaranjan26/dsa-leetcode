# strStr 

# haystack = "hello", needle = "ll"
# Output: 2

# Approach 1
def strStr(haystack, needle): 
    if not needle:
        return 0
    
    if not haystack:
        return -1
    
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            
            # slice the haystack from the current index to the length of the needle
            if haystack[i:i+len(needle)] == needle:
                return i
            
    return -1

if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    print(strStr(haystack, needle))
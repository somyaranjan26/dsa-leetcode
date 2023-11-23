# First Unique Character in a String

# Input: s = "leetcode"
# Output: 0

# Input: s = "aabb"
# Output: -1

# Solution 1: Using a dictionary
# Time Complexity: O(n), 
# because the time complexity of the for loop is O(n)
# Space Complexity: O(n), due to the dictionary
def firstUniqueChar(s):
    # create a dictionary
    d = {}
    
    # loop through the string
    for i in range(len(s)):
        # check if the character is in the dictionary
        if s[i] in d:
            # if the character is in the dictionary, increment the value by 1
            d[s[i]] += 1
        else:
            # if the character is not in the dictionary, add it to the dictionary with a value of 1
            d[s[i]] = 1
    
    # loop through the dictionary
    for i in range(len(s)):
        # check if the value of the character is 1
        if d[s[i]] == 1:
            # if the value of the character is 1, return the index of the character
            return i
    
    # if the value of the character is not 1, return -1
    return -1

# Solution 2: Using a dictionary and a list
def firstUniqueChar2(s):
    # create a dictionary
    d = {}
    
    # create a list
    l = []
    
    # loop through the string
    for i in range(len(s)):
        # check if the character is in the dictionary
        if s[i] in d:
            # if the character is in the dictionary, increment the value by 1
            d[s[i]] += 1
        else:
            # if the character is not in the dictionary, add it to the dictionary with a value of 1
            d[s[i]] = 1
            
            # add the character to the list
            l.append(s[i])
    
    # loop through the list
    for i in range(len(l)):
        # check if the value of the character is 1
        if d[l[i]] == 1:
            # if the value of the character is 1, return the index of the character
            return s.index(l[i])
    
    # if the value of the character is not 1, return -1
    return -1
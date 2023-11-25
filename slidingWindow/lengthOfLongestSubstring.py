# Length of Longest Substring  without repeating characters

# Given a string, find the length of the longest substring without repeating characters.
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

def lengthOfLongestSubstring1(s):
    result = -float('inf')
    length = len(s)
    substring = ''
    
    for l in range(length):
        print()
        for r in range(l, length):
            print("l, r :",s[l], s[r])
            if s[r] not in substring:
                substring += s[r]
            else:
                result = max(len(substring), result)
                substring = substring.replace(s[r], '')
                substring += s[r]
                break
    print(substring)
    return result

def lengthOfLongestSubstring2(s):
    result = -float('inf')
    length = len(s)
    substring = set()
    l = 0
    
    for r in range(length):
        
        while s[r] in substring:
            substring.remove(s[l])
            l += 1
        
        substring.add(s[r])
        result = max((r - l + 1), result)

    return result            
        
        


s = "abctyabcbb"
print(lengthOfLongestSubstring2(s))
# length Of Longest Substring Two Distinct Characters

# Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

# ! Example 1:
# Input: "eceba"
# Output: 3

# ? Explanation: t is "ece" which its length is 3.

def lengthOfLongestSubstringTwoDistinct(s):
    result, l = 0, 0
    hash = dict()
    
    for r in range(len(s)):
        hash[s[r]] = r
        
        if len(hash) == 3:
            # delete the leftmost character
            del_idx = min(hash.values())
            del hash[s[del_idx]]
            # move left pointer of the slidewindow
            l = del_idx + 1
        
        result = max((r - l + 1), result)
    
    return result

s = "eceba"
print(lengthOfLongestSubstringTwoDistinct(s))
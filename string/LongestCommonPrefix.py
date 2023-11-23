# Longest Common Prefix

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

def longestCommonPrefix(strs):
    result = ""
    if not strs:
        return result
    
    # loop through the first string
    for i in range(len(strs[0])):
        
        # loop through the rest of the strings from index 1 to the end
        for j in range(1, len(strs)):
            
            # if the index is greater than the length of the string or the character at the index is not the same as the first string
            if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                return result
            
        # if the character is the same, add it to the result    
        result += strs[0][i]
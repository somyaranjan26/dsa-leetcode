# Reverse String

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Title: 4 approaches based on different data structures for interview

# Intuition: 
# Used 4 different solutions to reverse a string. 
# 1. Using in-built function
# 2. Using two pointers
# 3. Using stack
# 4. Using recursion
# But the most efficient solution is using two pointers. 
# The time complexity is O(n/2) = O(n) and the space complexity is O(1). 

# Approach 1: Using in-built function
# - Time complexity: O(n) 
# - Space Complexity: O(1)
def reverseString1(s):
    s.reverse()
    
# Approach 2: Using two pointers
# - Time Complexity: O(n/2) = O(n)
# - Space Complexity: O(1)
def reverseString2(s):
    r = len(s)-1
    for l in range(len(s)//2):
        s[l], s[r] = s[r], s[l]
        r -= 1

# Approach 3: Using stack
# - Time Complexity: O(n)
# - Space Complexity: O(n)
def reverseString3(s):
    stack = []
    
    for i in range(len(s)):
            stack.append(s.pop())
    
    for i in range(len(stack)):
        s.append(stack[i])


# Approach 4: Using recursion
# - Time Complexity: O(n)
# - Space Complexity: O(n)
def reverseString4(s):
    def helper(l, r):
        if l < r:
            s[l], s[r] = s[r], s[l]
            helper(l+1, r-1)
    helper(0, len(s)-1) 


        
if __name__ == '__main__':
    s = ["h","e","l","l","o","o"]
    reverseString3(s)
    print(s)
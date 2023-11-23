# Valid Anagram

# Input: s = "anagram", t = "nagaram"
# Output: true

# Input: s = "rat", t = "car"
# Output: false

# Approach 1: Sort
# Time complexity: O(nlogn) where n is the length of s or t.
# Space complexity: O(1) or O(n) 
def isAnagram(s, t):
    return sorted(s) == sorted(t)

# Approach 2: Hash Table
# Time complexity: O(n) where n is the length of s or t. 
# Space complexity: O(1) or O(n) because the table size is fixed.
def isAnagram2(s, t):
    dict = {}

    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    
    for i in t:
        if i in dict:
            dict[i] -= 1
        else:
            return False
    
    for i in dict:
        if dict[i] != 0:
            return False
    
    return True

# Approach 3: Lambda function
# Time complexity: O(n) where n is the length of s or t. 
# Space complexity: O(1) or O(n) because the table size is fixed.
# ? lambda function is a small anonymous function. 
isAnagram3 = lambda s, t: sorted(s) == sorted(t)

# Approach 4: Array
# Time complexity: O(n) where n is the length of s or t.
# Spae complexity: O(1) or O(n) because the table size is fixed.
def isAnagram4(s, t):
    for i in set(s):
        if s.count(i) != t.count(i):
            return False
    return True

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))

    s = "rat"
    t = "car"
    print(isAnagram(s, t))

    s = "anagram"
    t = "nagaram"
    print(isAnagram2(s, t))

    s = "rat"
    t = "car"
    print(isAnagram2(s, t))

    s = "anagram"
    t = "nagaram"
    print(isAnagram3(s, t))

    s = "rat"
    t = "car"
    print(isAnagram3(s, t))

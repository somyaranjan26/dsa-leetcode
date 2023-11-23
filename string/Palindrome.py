# Valid Palindrome

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Approach 1: Two Pointers
def isPalindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        # ? isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False.
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1
    
    return True

if __name__ == '__main__':

    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))
    
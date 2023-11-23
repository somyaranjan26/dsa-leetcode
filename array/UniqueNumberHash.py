# 1207. Print Unique Number

# Input: arr = [1,2,2,1,1,3]
# Output: 3

def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # set() returns a set of unique elements
    # return true if the length of the set is not equal to the length of the list
    return len(nums) != len(set(nums))

def uniqueNumberHash(arr):
    dic = {}
    
    for i in arr:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
            
    print(dic)            
    # storing the key in result list if the value is 1
    # ? dic.items() returns a list of tuples of key and value
    print(dic.items())
    for key, value in dic.items(): 
        if value == 1:
            return key

if __name__ == "__main__":
    arr = [1,2,2,1,1,3]
    print(uniqueNumberHash(arr))
    # print(containsDuplicate(arr))
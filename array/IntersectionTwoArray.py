# 350. Intersection of two arrays

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]


# Solution 1
# Time complexity: O(n) dictionary operations are O(1) and for loop is O(n)
# Space complexity: Space of result list is O(n) and space of dictionary is O(n) total is O(2n) which is O(n)
def intersect(nums1, nums2):
    # create a dictionary to store the count of each element in nums1
    dic = {}
    
    # create a list to store the intersection
    result = []
    
    # for each element in nums1
    for i in nums1:
        # if the element is in the dictionary
        if i in dic:
            # increment the count of the element by 1
            dic[i] += 1
        else:
            # else, add the element to the dictionary with a count of 1
            dic[i] = 1
    
    print(dic)
    
    # for each element in nums2
    for i in nums2:
        # if the element is in the dictionary and the count of the element is greater than 0
        if i in dic and dic[i] > 0:
            # add the element to the result list
            result.append(i)
            # decrement the count of the element by 1
            dic[i] -= 1
    
    # return the result list
    return result

# Solution 2
# Time complexity: O(n) remove() is O(n) but it is called n times so it is O(n*n) = O(n)
# Space complexity: Space of the result list is O(n)
def intersection(nums1, nums2):
    result = []
    
    if len(nums1) < len(nums2):
        for i in nums1:
            if i in nums2:
                result.append(i)
                nums2.remove(i)
    else:
        for i in nums2:
            if i in nums1:
                result.append(i)
                nums1.remove(i)
    
    return result

# Solution 2 is better than solution 1 because it has a lower space complexity

if __name__ == "__main__":
    nums1 = [1,2,2,1] 
    nums2 = [2,2]
    print(intersect(nums1, nums2))
    print(intersection(nums1, nums2))
    
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(intersect(nums1, nums2))
    print(intersection(nums1, nums2))
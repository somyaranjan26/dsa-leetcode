# Two Sum

# Input: nums = [3,3], target = 6
# Output: [0,1]

# Solution 1: Brute Force
# Time Complexity: O(n) where n is the number of elements in nums 
# Space Complexity: O(n) where n is the number of elements in nums, due to the dictionary
def twoSum(nums, target):
    # create a dictionary to store the values
    # and their indices
    dict = {}
    
    # for each element in nums
    for i in range(len(nums)):
        
        # check if the difference between the target
        # and the current element is in the dictionary
        if target - nums[i] in dict:
            
            print(dict[target - nums[i]], dict[nums[i]])
            
            # return the indices of the current element
            # and the element that adds up to the target
            return [dict[target - nums[i]], i]
        
        # add the current element to the dictionary
        # along with its index
        dict[nums[i]] = i


# Solution 2: 
# Time Complexity: O(n) where n is the number of elements in nums 
# Space Complexity: O(n) where n is the number of elements in nums and the result list
def twoSum1(nums, target):
        
    for i in range(len(nums)):
            
        try:
            indexValue = nums.index(target - nums[i])
            
            # Check if the indexValue is equal to the current index    
            if indexValue == i:
                indexValue = -1
                continue
            
        except ValueError:
                indexValue = -1
                
        if indexValue != -1:
            return [i, indexValue]
                
    

if __name__ == "__main__":
    nums = [1, 2, 3, 0, 7 ,3]
    target = 6
    print(twoSum(nums, target))
    # print(twoSum1(nums, target))
# Minimum Size Subarray Sum

# ? target = 8, nums = [2,3,1,4,3]
# ? Output = 2


# Approach 1: Brute Force
# Time Complexity: O(n^2) where n is the number of elements in nums
# Space Complexity: O(1) because we are not using any extra space
def minSizeArraySum1(target, nums):
    result = float('inf') # infinity for storing the 1st minimum value
    temp = 0 # to count the number of elements
    total = 0 # to store the sum of the elements
    length = len(nums) # length of the array
    
    for i in range(length):
        temp = 0
        total = 0
        for j in range(i, length):
            if total <= target:  # if the sum of the elements is less than or equal to the target
                total += nums[j]  # add the element to the total
                temp += 1  # increment the number of elements
            
            if total >= target and temp < result:  # ! if the count of elements is less than the result and the total is greater than or equal to the target
                result = temp  # ! update the result with the number of elements
                break
        
        # ! if the result is infinity and the total is less than the target
        # inside i loop, we are avoiding the unnecessary iterations
        if result == float('inf') and total < target: 
            return 0
                
    return result


def minSizeArraySum2(target, nums):
    result = float('inf')
    
    return result

target = 17
# nums = [4,3,2,3,1]
nums = [1,1,1,1,1,1,1,1]
print(minSizeArraySum1(target, nums))
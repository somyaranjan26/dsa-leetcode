# 26. Remove Duplicates from Sorted Array

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2

def removeDuplicates(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1

if __name__ == "__main__":
    nums = [1,1,2]
    print(removeDuplicates(nums))
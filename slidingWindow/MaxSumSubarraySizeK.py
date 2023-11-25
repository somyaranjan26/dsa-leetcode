# Max Sum Subarray of Size K (easy)
# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

# Sliding Window Pattern
# Time Complexity: O(n) where n is the number of elements in arr
# Space Complexity: O(1) because we are not using any extra space

def maxSumSubArr(size, arr):
    result, sum, i = 0, 0, 0
    
    # ? j is the right pointer
    for j in range(len(arr)):
        
        # ? adding new element to the sum
        sum += arr[j]
        
        # ? if the window size is less than the size of the array then we go next element
        if j-i+1 < size:
            continue # right ++
        
        # ? if the window size is equal to the size of the array then we find the maximum sum
        elif j-i+1 == size:
            result = max(sum, result)
            
            # removing i element from the sum and incrementing i
            sum -= arr[i]
            i += 1

    return result

size = 3
arr = [13,6,17,1,8,3,7,8,8]
print(maxSumSubArr(size, arr))
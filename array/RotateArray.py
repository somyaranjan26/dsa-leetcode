# 189. Rotate Array

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]

def rotate(nums, k):
    i = 0
    
    # loop until i is less than k
    while i < k:
        # remove last element and store it in a
        a = nums.pop()
        
        # insert a at the beginning of the list
        nums.insert(0, a)
        
        # increment i
        i += 1
        
    return nums


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(rotate(nums, k))
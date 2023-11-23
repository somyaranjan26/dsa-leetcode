#  Move Zeroes

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Input: nums = [0]
# Output: [0]

# Title: [Python] 2 Solutions with O(n) and O(n^2) Time Complexity

# Intuition: 
# Solution 1: remove the zeros from the list and append them to the end of the list. 
# Solution 2: count the number of zeros and remove them from the list. Then add the number of zeros to the end of the list.
# Solution 2: is more efficient because it doesn't use the remove() method which is O(n) 
# and it doesn't create a new list and copy all the elements to it like nums = [i for i in nums if i != 0] does.

# Approach: 
# Solution 1: nested for loop and remove() method. 
# Solution 2: count the number of zeros and remove them from the list. Then add the number of zeros to the end of the list.



# Solution 1: 
def moveZeroes(nums):
    # ? for each element in nums
    for i in range(len(nums)):
        # ? if the element is 0
        if nums[i] == 0:
            # ? remove the element from the list
            nums.remove(0)
            # ? append 0 to the end of the list
            nums.append(0)
    return nums
# ! Time complexity: O(n^2) because of the nested for loop and the remove() method which is O(n)
# ! Space complexity: O(1) because we are not using any extra space

# Solution 2: count the number of zeros and remove them from the list
def moveZeroes2(nums):
        # ? count the number of zeros
    count = nums.count(0)
    print(count)
        # ? remove all the zeros from the list
        # ? nums[:] = [i for i in nums if i != 0] is the same as nums = [i for i in nums if i != 0], 
        # but nums[:] is more efficient because it doesn't create a new list 
        # and copy all the elements to it like nums = [i for i in nums if i != 0] does
    nums[:] = [i for i in nums if i != 0]
    print(nums)
        # ? add the number of zeros to the end of the list
        # ? nums += [0] * count is the same as nums = nums + [0] * count, 
        # but nums += [0] * count is more efficient because it doesn't create a new list and copy all the elements to it like nums = nums + [0] * count does
    nums += [0] * count
    return nums
# ! Time complexity: O(n) because of the for loop and the count() method which is O(1)
# ! Space complexity: O(1) because we are not using any extra space


if __name__ == '__main__':
    # print(moveZeroes([0,1,0,3,12]))
    print(moveZeroes2([0,1,0,3,12]))
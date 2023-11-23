# Binary Search Algorithm
# It is a search algorithm which works on the principle of divide and conquer to search for a particular element in a sorted array by repeatedly dividing the search interval in half

# Condition: Array must be sorted

# Time Complexity is O(logn)
# Space Complexity is O(1)

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# key = 7

def binarySearch(arr, key):
    l = 0
    r = len(arr) - 1

    while l <= r:
        
        # adding l and r may cause overflow
        # example: l = 2^31 - 1, r = 2^31 - 1
        mid = l + (r - l) // 2
        
        if key == arr[mid]:
            return mid
        
        elif key < arr[mid]:
            r = mid - 1
        
        else:
            l = mid + 1
        
    return -1

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 10
    
    print(binarySearch(arr, key))
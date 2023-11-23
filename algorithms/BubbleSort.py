# Bubble Sort Algorithm

# Comparison based sorting algorithm which means that the algorithm compares the elements to be sorted
# Stable sorting algorithm which means that the relative order of the elements is maintained
# In-place sorting algorithm which means that the algorithm does not require any extra space

# Total number of swaps is O(n^2) in the worst case and O(n) in the best case
# Total number of comparisons is O(n^2) in the worst case and O(n) in the best case

# Time Complexity is O(n^2)
# Space Complexity is O(1)

# Input arr = [3, 65 , 34, 2, 56, 34]
# Output arr = [2, 3, 34, 34, 56, 65]

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1] , arr[j]
    
    return arr

if __name__ == "__main__":
    arr = [3, 65 , 34, 2, 56, 34]
    print("Sorted: ", bubbleSort(arr))
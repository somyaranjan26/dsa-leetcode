

# Selection Sort Algorithm

# Comparison based sorting algorithm which means that the algorithm compares the elements to be sorted
# Stable sorting algorithm which means that the relative order of the elements is maintained
# In-place sorting algorithm which means that the algorithm does not require any extra space

# Total number of swaps is O(n) in the both worst case and best case
# Total number of comparisons is O(n^2) in the worst case and O(n) in the best case

def SelectionSortForLoop(arr):
    n = len(arr)
    
    # loop through the array
    for i in range(n):
        
        # initialize the minimum index to the current index
        min_idx = i
        
        # loop through the array to find the minimum element
        for j in range(i+1, n):
            
            # if the current element is less than the minimum element
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # swap the minimum element with the current element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr


if __name__ == "__main__":
    arr = [3, 65 , 34, 2, 56, 32]
    print("Sorted For Loop: ", SelectionSortForLoop(arr))

            
    
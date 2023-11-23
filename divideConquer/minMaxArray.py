
def findMinMax(arr, i, j):
    min = 0
    max = 0
    
    # ! handle single element
    if i == j:
        min = max = arr[i]
        
    # ! handle small problem (two element)
    elif i == j-1:
        if arr[i] < arr[j]:
            min = arr[i]
            max = arr[j]
        else:
            min = arr[j]
            max = arr[i]

    # ! handle big problem
    else:
        # Divide and Conquer approach
        # ? Divide
        mid = (i+(j-1))//2
        
        # ? Recursion -> Conquer
        min1, max1 = findMinMax(arr,i, mid)
        min2, max2 = findMinMax(arr, mid+1, j)
        
        # ? Combine
        if min1 < min2:
            min = min1
        else:
            min = min2
        
        if max1 < max2:
            max = max2
        else:
            max = max1
    
    return min, max


arr = [23,45,76,56,76,43,65,92,28,343]
i = 0
j = len(arr) - 1

min_val, max_val = findMinMax(arr, i, j)
print("Min and Max: ", min_val, max_val)
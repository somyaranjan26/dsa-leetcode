# Insertion Sort Algorithm

# Key, j

def insertionSort(arr):
    
    #  loop through the array from index 1 to the end
    for i in range(1, len(arr)):
        
        # key is the current element
        # key = 5
        key = arr[i]
        
        # j is the previous element
        # j = 0
        j = i-1
        
        # while j is greater than or equal to 0 and the key is less than the previous element
        #   j = 0 and key = 5 and arr[j] = 2
        while j >= 0 and key < arr[j]:
            # assign the previous element to the current element
            arr[j+1] = arr[j]
            # decrement j by 1 to move to the next element
            j -= 1
            
        # assign the key to the current element
        # arr[0+1] = 5  
        arr[j+1] = key
        
if __name__ == "__main__":
    arr = [2, 5, 1, 3, 4]
    print("Given: ",arr)
    insertionSort(arr)
    print("Sorted: ",arr)
        
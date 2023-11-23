# Ternary Search Algorithm
# It is a search algorithm which works on the principle of divide and conquer to search for a particular element in a sorted array by repeatedly dividing the search interval in 3 parts

# Condition: Array must be sorted

# Time Complexity is O(log3(n))
# Space Complexity is O(1)

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# key = 7

def ternarySearch(arr, key):
    l = 0
    r = len(arr) - 1
    
    while l <= r:
        
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3
        
        if key == arr[mid1]:
            return mid1
        
        elif key == arr[mid2]:
            return mid2
        
        elif key < arr[mid1]:
            r = mid1-1
        
        elif key > arr[mid2]:
            l = mid2+1
            
        else:
            l = mid1+1
            r = mid2-1
        
    return -1
    

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 6
    
    print(ternarySearch(arr, key))
    
''' 
Recurrence Relation

T(n) = T(n/3) + C
     = T(n/3^2) + 2C // for 2 recursive calls
     = T(n/3^3) + 3C // for 3 recursive calls
     
        for k recursive calls
     = T(n/3^k) + kC // for k recursive calls
     
         n/3^k = 1
         n = 3^k
         k = log3(n)
    
     = T(n/3^log3(n)) + log3(n).C
     = T(n/n^log3(3)) + log3(n).C
     = T(n/n^1) + log3(n).C
     = T(1) + log3(n).C
     
T(n) => O(log3(n))
'''
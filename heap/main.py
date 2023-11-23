import heapq 
# heapq is a min heap which means the smallest element is at the top

data = [10, 23, 65, 3, 56, 2, 12, 4, 8, 98]

# print(sorted(data)) ? Time complexity for inserting a new element is O(n)

heapq.heapify(data) # [2, 3, 10, 4, 56, 65, 12, 23, 8, 98]
# ? Time complexity for inserting a new element is O(log n)
# ! Index of left child = 2 * index of parent(i) + 1
# ! Index of right child = 2 * index of parent(i) + 2

print("-"*20)
print("Heapify")

print("DATA: ",data)

copy = data[:]
# ? [:] is a shallow copy of the list if we not use [:] then it will be a deep copy
# ! shallow copy means if we change the value of the copy then the original list will also be changed
# ! deep copy means if we change the value of the copy then the original list will not be changed

print("COPY: ",copy)

print("-"*20)
print("Heap POP")

print(heapq.heappop(data)) # ? Time complexity for removing an element is O(log n) and it will remove the smallest element (root node)
print(copy.pop(0)) # ? Time complexity for removing an element is O(n) and it will remove the first element

# differnce between heapq.heappop(data) and copy.pop(0) is that heapq.heappop(data) will remove the smallest element and copy.pop(0) will remove the first element
# and heappop will also maintain the heap property 

print("-"*20)
print("DATA: ",data)
print("COPY: ",copy)

print("-"*20)
print("Heap PUSH")

heapq.heappush(data, 45) # ? Time complexity for inserting a new element is O(log n) and it will insert the element at the right position
heapq.heappush(data, 100)
print("DATA: ",data)

print("-"*20)
print("MAX HEAP")
heapq._heapify_max(data)
print("DATA: ",data)

print("-"*20)

print("MAX HEAP POP")
print(heapq._heappop_max(data))

print("-"*20)
print("DATA: ",data)

print("-"*20)

print("Merge")

l1 = [14,52,43,45,24]
l2 = [43,6,165,23,190,2,7,4,8,5]
data3 = heapq.merge(l1, l2) # ? Time complexity for merging two lists is O(n)

print(list(data3))

print("-"*20)


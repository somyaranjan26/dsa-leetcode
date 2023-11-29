import collections
import heapq

def topKFreq(nums, k):
    counter = collections.Counter(nums)
    print(counter)
    
    heap = [(val, key) for key, val in counter.items()]
    print(heap)
    
    heapq.heapify(heap)
    print(heap)
    
    heap = heapq.nlargest(k, heap)
    print("Temp: ",heap)
    
    # ? freq is the first element in the tuple
    return [ nums for (freq, nums) in heap]
    
    
if "__main__" == __name__:
    nums = [1,1,1,1,1,1,1,2,2,2,3]
    k = 2
    print(topKFreq(nums, k))
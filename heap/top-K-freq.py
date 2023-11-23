import collections
import heapq

def topKFreq(nums, k):
    counter = collections.Counter(nums)
    print(counter)
    
    heap = [(val, key) for key, val in counter.items()]
    print(heap)
    
    heapq.heapify(heap)
    print(heap)
    
    while len(heap)-1 > 0:
        print(heapq.heappop(heap)[1])
        print(heap)
        k -= 1
        
    return [ nums for (freq, nums) in heap]
    
    
if "__main__" == __name__:
    nums = [1,1,1,1,1,1,1,2,2,2,3]
    k = 2
    print(topKFreq(nums, k))
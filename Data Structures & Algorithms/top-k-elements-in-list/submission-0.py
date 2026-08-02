import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}

        for num in nums:
            freqDict[num] = freqDict.get(num, 0) + 1
        
        heap = []
        for key, value in freqDict.items():
            heap.append((value, key))
        heapq.heapify(heap)
        topK = heapq.nlargest(k, heap)
        print(topK)
        result = []
        for t in topK:
            result.append(t[1])
        return result
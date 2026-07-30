class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}

        for i, num in enumerate(nums):
            if i == 0:
                indexMap[num] = 0
            else:
                complement = target - num
                
                if complement in indexMap:
                    return [indexMap[complement], i]
                
                indexMap[num] = i
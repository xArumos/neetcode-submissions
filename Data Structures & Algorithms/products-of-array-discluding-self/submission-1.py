class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        singleZero = False
        doubleZero = False
        for num in nums:
            if num == 0:
                if singleZero:
                    doubleZero = True
                else:
                    singleZero = True
            else:
                total *= num
        
        result = []
        for num in nums:
            if doubleZero:
                result.append(0)
            elif singleZero and num == 0:
                result.append(total)
            elif singleZero and num != 0:
                result.append(0)
            else:
                result.append(total // num)
        
        return result
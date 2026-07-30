class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}

        for sChar in s:
            if sChar in sDict:
                sDict[sChar] += 1
            else:
                sDict[sChar] = 1
        for tChar in t:
            if tChar in tDict:
                tDict[tChar] += 1
            else:
                tDict[tChar] = 1
        
        if sDict == tDict:
            return True
        else:
            return False
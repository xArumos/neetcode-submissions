class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupingDict = {}
        for s in strs:
            count = [0] * 26

            for c in s:
                index = ord(c) - 97
                count[index] = count[index] + 1
            if str(count) not in groupingDict:
                groupingDict[str(count)] = [s]
            else:
                groupingDict[str(count)].append(s)
        result = []
        for key, value in groupingDict.items():
            result.append(value)

        return result
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            for c in s:
                encoded_string += (str(ord(c) + 100))
            encoded_string += "000"
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_string = []
        for i in range(len(s) // 3):
            if i == 0:
                tempString = ""
            iScaled = i * 3
            numSlice = s[iScaled:iScaled+3]
            if numSlice == "000":
                decoded_string.append(tempString)
                tempString = ""
            else:
                tempString += chr(int(numSlice) - 100)
                if iScaled + 3 == len(s):
                    decoded_string.append(tempString)
        return decoded_string
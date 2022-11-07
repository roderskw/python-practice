class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        symbols = set([])
        substring = ""
        actualSize = maxSize = 0
        for x in range(0, len(s)):
            if(set(s[x]) <= symbols):
                #maxSize = max(maxSize, actualSize)
                #print("found duplicate, current symbols - " + str(symbols) + ",current subtring - " + str(substring))
                substring = substring[substring.find(s[x]) + 1: x] + s[x]
                symbols = set(substring)
                #print("after  new set, current symbols - " + str(symbols) + ",current subtring - " + str(substring))
                actualSize = len(symbols)
                maxSize = max(maxSize, actualSize)
            else:
                symbols.add(s[x])
                substring = substring + s[x]
                actualSize += 1
                maxSize = max(maxSize, actualSize)
                #print("added symbol, maxSize = " + str(maxSize))
        return maxSize


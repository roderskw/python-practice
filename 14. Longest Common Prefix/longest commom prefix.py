class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort(key = lambda y : len(y)) #sorts with the smallest word on strs[0]
        same = True
        prefix = ""
        for i in range(0, len(strs[0])):
            prefix = prefix + strs[0][i]  #adds 1 letter of the first word in each itearation
            for x in strs:                #checks if this letter is present in others words
                if(x[i] != prefix[i]):
                    same = False
                    break
            if(same == False):
                prefix = prefix[0:i]      #removes last character that was tested wrong
                break
            i += 1
        return prefix
        
             
a = Solution()

strs = ["flower","flow","flight"]

print("expected = fl \noutput   = " + str(a.longestCommonPrefix(strs)))

strs = ["dog","racecar","car"]

print("expected =  \noutput   = " + str(a.longestCommonPrefix(strs)))

strs = ["flower","flow","flowers"]

print("expected = flow \noutput   = " + str(a.longestCommonPrefix(strs)))

strs = ["flower","flower","flower"]

print("expected = flower \noutput   = " + str(a.longestCommonPrefix(strs)))

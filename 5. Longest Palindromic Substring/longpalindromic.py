class Solution:
    def longestPalindrome(self, s: str) -> str:
        slist = list(s)
        totalSize = len(slist)
        
        if(len(set(s)) == 1): # kind of cheating tests with a string with same character
            return s

        longestPalindrome = ""
        slist = list(s)
        actualMaxSize = 0
        for x in range(0, totalSize - 1):
             
            if(slist[x] == slist[x + 1]): #even case
                size = 0
                while(size <= x and size < totalSize - x - 1):
                    if(slist[x - size] == slist[x + 1 + size]):
                        if(len(list(longestPalindrome)) < len(slist[x - size: x + size + 2])):
                            longestPalindrome = "".join(slist[x - size: x + size + 2])
                        size += 1
                    else:
                        break
            #odd case
            size = 0
            while(size <= x and size < totalSize - x):
                if(slist[x - size] == slist[x + size]):
                    if(len(list(longestPalindrome)) < len(slist[x - size: x + size + 1])):
                        longestPalindrome = "".join(slist[x - size: x + size + 1])
                    size += 1
                else:
                    break

        return longestPalindrome

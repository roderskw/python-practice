class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last  = len(s) - 1

        while( s[last] == " "):
            last -=1

        return(len(s[s[0:last].rfind(" ") + 1 : last + 1]))
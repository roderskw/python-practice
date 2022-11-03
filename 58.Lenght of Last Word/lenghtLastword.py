class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last  = len(s) - 1

        while( s[last] == " "):
            last -=1

        return(len(s[s[0:last].rfind(" ") + 1 : last + 1]))

a = Solution()

s = "a b c deded"

print("expected = 5 \noutput   = " + str(a.lengthOfLastWord(s)))

s = "   fly me to the moon"

print("expected = 4 \noutput   = " + str(a.lengthOfLastWord(s)))

s = "   fly me   to   the moon  "

print("expected = 4 \noutput   = " + str(a.lengthOfLastWord(s)))
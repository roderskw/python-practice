class Solution(object):
    def isSubsequence(self, s: str, t: str) -> bool:
        i = int(-1)
        for x in s:
            i = t.find(x, i + 1)
            if(i == -1):
                return False

        return True

a = Solution()
s = "axc"
t = "ahbgdc"

print("expected = False \noutput   = " + str(a.isSubsequence( s, t)))


ab = "abc"
b = "ahbgdc"

print("expected = True \noutput   = " + str(a.isSubsequence( ab, b)))

c = "aaaaaa"
d = "bbaaaa"

print("expected = False \noutput   = " + str(a.isSubsequence( c, d)))
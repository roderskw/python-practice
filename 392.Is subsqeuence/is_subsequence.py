class Solution(object):
    def isSubsequence(self, s: str, t: str) -> bool:
        i = int(-1)
        for x in s:
            i = t.find(x, i + 1)
            if(i == -1):
                return False

        return True
def isSubsequence(self, s: str, t: str) -> bool:
    currentMax = int(0)
    for x in s:
        if(t.find(x) == -1):  
            return False

        if(t.find(x) < currentMax): 
            return False 

        currentMax = t.find(x)
        
    return True


s = "axc"
t = "ahbgdc"

print(isSubsequence(0, s, t))


a = "abc"
b = "ahbgdc"

print(isSubsequence(0, a, b))

c = "aaaaaa"
d = "bbaaaa"

print(isSubsequence(0, c, d))
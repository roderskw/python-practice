def isAnagram(self, s: str, t: str) -> bool:
    if(len(s) != len(t)):
        return False
    for x in s:
        if(t.find(x) == -1): #character x is not present in t
            return False
        if(s.count(x) != t.count(t[t.find(x)]) ): #character x does not have the same occurences in t
            return False
    return True


# variable.count("apple") Return the number of times the value "apple" appears in the string variable

a = 0

s = "anagram"
t = "nagaram"

print(isAnagram(a, s, t))

s = "rat"
t = "car"

print(isAnagram(a, s, t))





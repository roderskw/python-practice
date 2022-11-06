import valid_anagram

def testcases(exp: str, s: valid_anagram.Solution, ss: str, t: str):
    print("--------------- Teste iniciado ---------------")
    print("expected = " + str(exp) + "\noutput   = " + str(s.isAnagram(ss, t)))
    
    print("--------------- Teste finalizado ---------------")

s = valid_anagram.Solution()

ss = "anagram"
t = "nagaram"
testcases("True", s, ss, t)

ss = "rat"
t = "car"
testcases("False", s, ss, t)

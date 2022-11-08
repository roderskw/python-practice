import is_subsequence

def testcases(exp: str, s: is_subsequence.Solution, ss: str, t: str):
    print("--------------- Teste iniciado ---------------")
    print("expected = " + str(exp) + "\noutput   = " + str(s.isSubsequence(ss, t)))
    
    print("--------------- Teste finalizado ---------------")

s = is_subsequence.Solution()

ss = "axc"
t = "ahbgdc"
testcases("False", s, ss, t)

ss = "abc"
t = "ahbgdc"
testcases("True", s, ss, t)

ss = "aaaaaa"
t = "bbaaaa"
testcases("False", s, ss, t)
import substring

def testcases(exp: str, s: substring.Solution, ss: str):
    print("--------------- Teste iniciado ---------------")
    print("expected = " + str(exp) + "\noutput   = " + str(s.lengthOfLongestSubstring(ss)))
    
    print("--------------- Teste finalizado ---------------")

s = substring.Solution()

ss = "abcabcbb"
testcases("3", s, ss)

ss = "bbbbb"
testcases("1", s, ss)

ss = "pwwkew"
testcases("3", s, ss)

ss = "aab"
testcases("2", s, ss)
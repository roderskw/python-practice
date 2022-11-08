import longpalindromic
def testcases(exp: str, sol: longpalindromic.Solution, ss: str):
    print("--------------- Teste iniciado ---------------")
    print("expected = " + str(exp) + "\noutput   = " + str(sol.longestPalindrome(ss)))
    
    print("--------------- Teste finalizado ---------------")

s = longpalindromic.Solution()

ss = "babad"
testcases("bab or aba", s, ss)

ss = "cbbd"
testcases("bb", s, ss)

ss = "ac"
testcases("a", s, ss)

ss = "bb"
testcases("bb", s, ss)

ss = "ccc"
testcases("ccc", s, ss)

ss = "c"
testcases("c", s, ss)
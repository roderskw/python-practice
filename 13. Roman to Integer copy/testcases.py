import roman

def testcases(exp: str, s: roman.Solution, ss: str):
    print("--------------- Teste iniciado ---------------")
    print("expected = " + str(exp) + "\noutput   = " + str(s.romanToInt(ss)))
    
    print("--------------- Teste finalizado ---------------")

s = roman.Solution()

ss = "III"
testcases("3", s, ss)

ss = "LVIII"
testcases("58", s, ss)

ss = "MCMXCIV"
testcases("1994", s, ss)

ss = "IV"
testcases("4", s, ss)

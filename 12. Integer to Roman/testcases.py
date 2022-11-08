import int_roman

def testcases(exp: str, s: int_roman.Solution, num: int):
    print("--------------- Teste iniciado ---------------")
    print("expected = " + str(exp) + "\noutput   = " + str(s.intToRoman(num)))
    
    print("--------------- Teste finalizado ---------------")

s = int_roman.Solution()

num = 3
testcases("III", s, num)

num = 58
testcases("LVIII", s, num)

num = 1994
testcases("MCMXCIV", s, num)

num = 4
testcases("IV", s, num)

num = 9
testcases("IX", s, num)
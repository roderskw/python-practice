import lenght_last_word

def testcases(exp: str, s: lenght_last_word.Solution, strr: str):
    print("--------------- Teste iniciado ---------------")
    print("expected = " + str(exp) + "\noutput   = " + str(s.lengthOfLastWord(strr)))
    
    print("--------------- Teste finalizado ---------------")
 
s = lenght_last_word.Solution()

strr = "a b c deded"
testcases("5", s, strr)

strr = "   fly me to the moon"
testcases("4", s, strr)

strr = "   fly me   to   the moon  "
testcases("4", s, strr)


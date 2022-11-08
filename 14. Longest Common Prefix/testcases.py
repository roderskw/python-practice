import longest_prefix

def testcases(exp: str, s: longest_prefix.Solution, strs: list[str]):
    print("--------------- Teste iniciado ---------------")
    print("expected = " + str(exp) + "\noutput   = " + str(s.longestCommonPrefix(strs)))
    
    print("--------------- Teste finalizado ---------------")

s = longest_prefix.Solution()

strs = ["flower","flow","flight"]
testcases("fl", s, strs)

strs = ["dog","racecar","car"]
testcases("", s, strs)

strs = ["flower","flow","flowers"]
testcases("flow", s, strs)

strs = ["flower","flower","flower"]
testcases("flower", s, strs)
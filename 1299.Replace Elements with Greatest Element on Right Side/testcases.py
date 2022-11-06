import replace_element

def testcases(exp: str, s: replace_element.Solution, arr: list[int]):
    print("--------------- Teste iniciado ---------------")
    print("expected = " + str(exp) + "\noutput   = " + str(s.replaceElements(arr)))
    
    print("--------------- Teste finalizado ---------------")

s = replace_element.Solution()

arr = [17,18,5,4,6,1]
testcases("[18, 6, 6, 6, 1, -1]", s, arr)

arr = [400]
testcases("[-1]", s, arr)

import mostwater

def testcases(exp: str, s: mostwater.Solution, nums: list[int]):
    print("--------------- Teste iniciado ---------------")
    print("expected = " + str(exp) + "\noutput   = " + str(s.maxArea(nums)))
    
    print("--------------- Teste finalizado ---------------")

s = mostwater.Solution()

nums = [1,8,6,2,5,4,8,3,7]
testcases("49", s, nums)

nums = [1,1]
testcases("1", s, nums)
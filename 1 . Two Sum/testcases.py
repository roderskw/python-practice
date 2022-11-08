import two_sum

def testcases(exp: str, s: two_sum.Solution, nums: int , target: int):
    print("--------------- Teste iniciado ---------------")
    print("expected = " + str(exp) + "\noutput   = " + str(a.twoSum(nums, target)))
    
    print("--------------- Teste finalizado ---------------")

a = two_sum.Solution()

nums = [2,7,11,15]
target = 9
testcases("[0, 1]", a, nums, target)

nums = [3,2,4]
target = 6
testcases("[1, 2]", a, nums, target)

nums = [3,3]
target = 6
testcases("[0, 1]", a, nums, target)

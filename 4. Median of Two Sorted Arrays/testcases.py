import medianarrays
def testcases(exp: str, s: medianarrays.Solution, nums1: list[int], nums2: list[int]):
    print("--------------- Teste iniciado ---------------")
    print("expected = " + str(exp) + "\noutput   = " + str(s.findMedianSortedArrays(nums1, nums2)))
    
    print("--------------- Teste finalizado ---------------")

s = medianarrays.Solution()

nums1 = [1,3]
nums2 = [2]
testcases("2.00000", s, nums1, nums2)

nums1 = [1,2]
nums2 = [3,4]
testcases("2.50000", s, nums1, nums2)


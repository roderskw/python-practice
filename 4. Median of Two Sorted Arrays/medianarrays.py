class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        total = len(nums1) + len(nums2) 

        for x in range(0, int((total + 1)/2)):
            if(len(nums2) == 0):
                median = nums1[0] 
                nums1.pop(0)
            elif(len(nums1) == 0):
                median = nums2[0] 
                nums2.pop(0)
            elif(nums1[0] <= nums2[0]):
                median = nums1[0]
                nums1.pop(0)
            else:
                median = nums2[0] 
                nums2.pop(0)

        if(total%2 == 1):
            return float(median)
        else:
            if(len(nums2) > 0 and len(nums1) > 0):
                return float((median + min(nums1[0], nums2[0]))/2)
            elif(len(nums1) > 0):
                return float((median + nums1[0])/2)
            else:
                return float((median + nums2[0])/2)

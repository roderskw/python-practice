class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for x in range(0, len(nums) - 1):
            qty = nums[x + 1: len(nums)].count(target - nums[x])
            if(qty != 0):
                y =  nums[x + 1: len(nums)].index(target - nums[x])
                return [x,y + x + 1]
            

a = Solution()

nums = [2,7,11,15]
target = 9

print("expected = [0, 1] \noutput   = " + str(a.twoSum(nums, target)))

nums = [3,2,4]
target = 6

print("expected = [1, 2] \noutput   = " + str(a.twoSum(nums, target)))

nums = [3,3]
target = 6

print("expected = [0, 1] \noutput   = " + str(a.twoSum(nums, target)))


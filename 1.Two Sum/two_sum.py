class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for x in range(0, len(nums) - 1):
            qty = nums[x + 1: len(nums)].count(target - nums[x])
            if(qty != 0):
                y =  nums[x + 1: len(nums)].index(target - nums[x])
                return [x,y + x + 1]

class Solution:
    def maxArea(self, height: list[int]) -> int:
        x = 0
        y = len(height) - 1
        maxarea = 0

        while(x != y):
            maxarea = max(maxarea, min(height[x], height[y]) * abs(x-y))
            if(height[x] > height[y]):
                y -= 1
            else:
                x += 1

        return maxarea
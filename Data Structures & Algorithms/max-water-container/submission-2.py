class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0

        l, r = 0, len(heights) - 1

        while l < r:
            curWater = min(heights[l], heights[r]) * (r - l)
            maxWater = max(curWater, maxWater)
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
        return maxWater
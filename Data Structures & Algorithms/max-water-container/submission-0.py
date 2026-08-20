class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0, len(heights) - 1
        largest = 0

        while l < r:
            wall = min(heights[l], heights[r])
            area = wall * (r - l)
            if heights[r] < heights[l]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1
            elif heights[r] == heights[l]:
                l += 1
            largest = max(largest, area)
        return largest

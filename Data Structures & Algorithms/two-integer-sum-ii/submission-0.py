class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            diff = numbers[r] + numbers[l]
            if diff > target:
                r -= 1
            elif diff < target:
                l += 1
            elif diff == target:
                return [l + 1, r + 1]
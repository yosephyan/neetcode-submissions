class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, n in enumerate(nums):
            if n > 0:
                break
            if n == nums[i - 1] and i > 0:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threesum = n + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    result.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l +=1
        return result
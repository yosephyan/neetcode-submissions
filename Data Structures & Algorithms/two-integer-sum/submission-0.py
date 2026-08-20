class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            first = target - nums[i]
            if first in hashmap:
                return [hashmap[first], i]
            else:
                hashmap[nums[i]] = i
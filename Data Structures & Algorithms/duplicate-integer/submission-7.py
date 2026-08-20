class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        molla = set()
        for i in nums:
            if i in molla:
                return True
            molla.add(i)
        return False            
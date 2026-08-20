class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            count = 0
            for n in piles:
                rate = math.ceil(float(n) / k)
                count += rate
            if count > h:
                l = k + 1
            else:
                res = k
                r = k - 1
        return res

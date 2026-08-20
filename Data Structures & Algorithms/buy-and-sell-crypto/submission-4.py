class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            maxprofit = max(maxprofit, price - lowest)
        return maxprofit
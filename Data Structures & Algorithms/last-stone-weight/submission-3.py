class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            larger = heapq.heappop(stones)
            smaller = heapq.heappop(stones)
            diff = larger - smaller
            heapq.heappush(stones, diff)

        if not stones:
            return 0
        
        stones = [-s for s in stones]
        return stones[0]
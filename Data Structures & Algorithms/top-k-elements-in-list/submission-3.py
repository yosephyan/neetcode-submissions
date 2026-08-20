class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            hashmap[n] += 1
        
        for n, count in hashmap.items():
            freq[count].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
            if len(res) == k:
                return res
            
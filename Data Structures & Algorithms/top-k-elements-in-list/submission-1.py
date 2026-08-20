class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        array = [[] for i in range(len(nums) + 1)]

        for n in nums:
            dictionary[n] = dictionary.get(n, 0) + 1
        
        for n, c in dictionary.items():
            array[c].append(n)
        
        result = []
        for i in range(len(nums), 0, -1):
            for n in array[i]:
                result.append(n)
                if len(result) == k:
                    return result
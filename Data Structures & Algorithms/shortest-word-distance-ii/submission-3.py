class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.storewords = defaultdict(list)

        for i, word in enumerate(wordsDict):
            self.storewords[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        loc1 = self.storewords[word1]
        loc2 = self.storewords[word2]

        shortest = float('inf')
        l1, l2 = 0, 0

        while l1 < len(loc1) and l2 < len(loc2):
            shortest = min(shortest, abs(loc1[l1] - loc2[l2]))
            if loc1[l1] < loc2[l2]:
                l1 += 1
            else:
                l2 += 1


        return shortest


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

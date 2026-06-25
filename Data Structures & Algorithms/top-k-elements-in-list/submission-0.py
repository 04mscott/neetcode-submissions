from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)

        for num in nums:
            frequencies[num] += 1

        top_k = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)[:k]

        return [a for a, b in top_k]
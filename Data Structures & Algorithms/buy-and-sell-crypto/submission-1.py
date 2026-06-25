import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [0]
        min_seen = prices[0]
        for price in prices[1:]:
            min_seen = min(price, min_seen)
            profits.append(price - min_seen)
        return max(profits)
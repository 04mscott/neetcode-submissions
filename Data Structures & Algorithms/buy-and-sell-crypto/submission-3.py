class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_seen = prices[0]
        max_profit = 0
        for price in prices[1:]:
            min_seen = min(price, min_seen)
            max_profit = max(price - min_seen, max_profit)
        return max_profit
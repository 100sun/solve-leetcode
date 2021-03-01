class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # print(list(zip(prices[:-1], prices[1:])))
        return sum([y - x for x, y in zip(prices[:-1], prices[1:]) if x < y])
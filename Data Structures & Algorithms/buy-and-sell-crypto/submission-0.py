class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxmProfit = 0
        minmPrice = prices[0]

        for price in prices:
            minmPrice = min(minmPrice,price)
            maxmProfit = max(maxmProfit,price - minmPrice)

        return maxmProfit

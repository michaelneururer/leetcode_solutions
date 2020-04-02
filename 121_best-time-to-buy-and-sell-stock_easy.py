class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        sol = 0
        for i in range(1,len(prices)):
            if prices[i]-prices[buy] > sol:
                sell = i
                sol = prices[i]-prices[buy]
            if prices[i] < prices[buy]:
                buy = i
        return sol
        

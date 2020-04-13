import math
class Solution:
    def __init__(self):
        self.examples = [[3,3,5,0,0,3,1,4], [1,2,3,4,5], [7,6,4,3,1]]
        self.solutions = [6,4,0]
    def maxProfit(self, prices) -> int:
        if len(prices)==0:
            return 0
        n = len(prices)
        max_prices_from = [0 for i in range(n)]
        min_prices_until = [0 for i in range(n)]
        max_prices_from[n-1] = prices[n-1]
        min_prices_until[0] = prices[0]
        one_trans_from = [0 for i in range(n)] #max profit with one transaction STARTING at index i
        one_trans_until = [0 for i in range(n)] #max profit with one transaction UNTIL (including) index i
        for i in range(n-2,-1,-1):
            max_prices_from[i] = max(prices[i],max_prices_from[i+1])
            min_prices_until[n-1-i] = min(prices[n-1-i], min_prices_until[n-2-i])
            one_trans_from[i] = max(max_prices_from[i+1]-prices[i],one_trans_from[i+1])
            one_trans_until[n-1-i] = max(one_trans_until[n-2-i],prices[n-1-i] - min_prices_until[n-2-i])

        return max([one_trans_until[i-1] + one_trans_from[i] for i in range(1,n)]+[one_trans_from[0]])

    def test_examples(self):
        for i in range(len(self.examples)):
            print(self.maxProfit(self.examples[i]), self.maxProfit(self.examples[i])==self.solutions[i])

import math
class Solution:
    def __init__(self):
        self.examples = [[7,1,5,3,6,4], [1,2,3,4,5], [7,6,4,3,1]]
        self.solutions = [7,4, 0]
    def maxProfit(self, prices) -> int:
        if len(prices)==0:
            return 0
        n = len(prices)
        res = 0
        with_stock = [0 for i in range(n)] #Starting with stock at position i
        without_stock = [0 for i in range(n)] #Starting without stock at position i
        with_stock[n-1] = prices[n-1]
        for i in range(n-2,-1,-1):
            without_stock[i] = max(with_stock[i+1] - prices[i], without_stock[i+1])
            with_stock[i] = max(prices[i] + without_stock[i+1], with_stock[i+1])
        return without_stock[0]

    def test_examples(self):
        for i in range(len(self.examples)):
            print(self.maxProfit(self.examples[i]), self.maxProfit(self.examples[i])==self.solutions[i])

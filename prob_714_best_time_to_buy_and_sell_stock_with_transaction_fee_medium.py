import math
class Solution:
    def __init__(self):
        self.examples = [([1, 3, 2, 8, 4, 9],2)]
        self.solutions = [8]
    def maxProfit(self, prices, fee) -> int:
        if len(prices)==0:
            return 0
        n = len(prices)
        res = 0
        with_stock = [0 for i in range(n)] #Starting with stock at position i
        without_stock = [0 for i in range(n)] #Starting without stock at position i
        with_stock[n-1] = max(prices[n-1]-fee,0)
        for i in range(n-2,-1,-1):
            without_stock[i] = max(with_stock[i+1] - prices[i], without_stock[i+1])
            with_stock[i] = max(prices[i] + without_stock[i+1] - fee, with_stock[i+1])
            print(with_stock,without_stock)
        return without_stock[0]

    def test_examples(self):
        for i in range(len(self.examples)):
            print(self.maxProfit(self.examples[i][0],self.examples[i][1]), self.maxProfit(self.examples[i][0], self.examples[i][1])==self.solutions[i])

import math
import collections

class Solution:
    def maxSubArray(self, nums) -> int:
        n = len(nums)
        start = 0 #start of the array
        stop = 0
        tmp = nums[0] #sum of the numbers from start to i
        sol_sum = nums[0]
        for i in range(1,n):
            tmp += nums[i]
            if tmp > sol_sum:
                sol_sum = tmp
                stop = i

            if tmp <= 0:
                start = i+1
                tmp = 0
                continue
        return sol_sum

    def test_examples(self):
        print(self.maxSubArray(self, [-2,1,-3,4,-1,2,1,-5,4])==6)

import math
import collections

class Solution:
    def threeSum(self, nums):
        nums.sort()
        nonneg = collections.Counter([n for n in nums if n >= 0])
        neg = [n for n in nums if n < 0]
        n = len(nums)
        sol = [] if nonneg[0] < 3 else [[0,0,0]]
        for i in range(len(neg)):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if nums[j]+nums[i]>0:
                    break
                if (j > i+1 and nums[j] == nums[j-1]) or (nums[i]==-2*nums[j] and nonneg[nums[j]]<2) or nums[j]>-(nums[i]+nums[j]):
                    continue
                if -(nums[i]+nums[j]) in nonneg.keys():
                    sol.append([nums[i],nums[j],-(nums[i]+nums[j])])
        return sol

    def test_examples(self):
        print(self.threeSum(self,[-1, 0, 1, 2, -1, -4]))

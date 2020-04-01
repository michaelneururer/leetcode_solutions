import math
import collections

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        sol = sum([nums[i] for i in range(3)])
        end = len(nums)-1
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                if nums[i]+nums[j] >= target:
                    if abs(nums[i]+nums[j]+nums[j+1] - target)<abs(sol - target):
                        return nums[i]+nums[j]+nums[j+1]
                for k in range(j+1,end+1):
                    if abs(nums[i]+nums[j]+nums[k] - target)<abs(sol - target):
                        sol = nums[i]+nums[j]+nums[k]
                    if nums[i]+nums[j]+nums[k] >= target:
                        end = k
                        break
        return sol

    def test_examples(self):
        print(self.threeSumClosest(self,[-1, 2, 1, -4],1))
        print(self.threeSumClosest(self,[0,2,1,-3],1)) #Expected 0
        print(self.threeSumClosest(self,[-3,-2,-5,3,-4],-1)) #Expected -2
        print(self.threeSumClosest(self,[6,-18,-20,-7,-15,9,18,10,1,-20,-17,-19,-3,-5,-19,10,6,-11,1,-17,-15,6,17,-18,-3,16,19,-20,-3,-17,-15,-3,12,1,-9,4,1,12,-2,14,4,-4,19,-20,6,0,-19,18,14,1,-15,-5,14,12,-4,0,-10,6,6,-6,20,-8,-6,5,0,3,10,7,-2,17,20,12,19,-13,-1,10,-1,14,0,7,-3,10,14,14,11,0,-4,-15,-8,3,2,-5,9,10,16,-4,-3,-9,-8,-14,10,6,2,-12,-7,-16,-6,10],-52)) #Expected -52

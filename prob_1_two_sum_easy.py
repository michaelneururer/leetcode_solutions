from itertools import *
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target-nums[i] in nums:
                if i==nums.index(target-nums[i]):
                    continue
                return [i, nums.index(target-nums[i])]

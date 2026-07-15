class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for index, m in enumerate(nums):
            n = target - m
            
            if n in seen:
                return [seen[n], index]
            seen[m] = index
            
        return []
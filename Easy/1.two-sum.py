#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
import math

class Solution:
    def twoSum(self, nums, target: int):
        element1: int = 0
        element2: int = 0
        element_total: int = 0
        
        for base_index in range(len(nums) - 1):
            element1 = nums[base_index]
            
            for offset_index in range(base_index+1, len(nums)):
                element2 = nums[offset_index]
                element_total = element1 + element2
                
                if(element_total != target):
                    continue
            
                return [base_index, offset_index]
            
#obj = Solution()
#obj.twoSum([1,6142,8192,10239], 18431)
# @lc code=end
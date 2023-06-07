#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        value: str = str(x)
        left_index = 0
        right_index = len(value) - 1
        
        while left_index < right_index:
            if value[left_index] != value[right_index]:
                return False
            
            left_index += 1
            right_index -= 1
            
        return True
# @lc code=end

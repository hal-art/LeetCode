#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s) -> None:
        leftIndex = 0
        rightIndex = len(s) - 1 - leftIndex
        
        while leftIndex < rightIndex:
            tmp  = s[leftIndex]
            s[leftIndex] = s[rightIndex]
            s[rightIndex] = tmp
            
            leftIndex += 1
            rightIndex -= 1
# @lc code=end
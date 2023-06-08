#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        lcp = ""
        lcp = strs[0]
        for i, str in enumerate(strs):
            if i == 0:
                continue
            
            lcp = self.__getLCPByTwoStrs(lcp, str)
            if lcp == '':
                break
        
        return lcp
        
    def __getLCPByTwoStrs(self, str1:  str, str2: str) -> str:
        length = min(len(str1), len(str2)) 
        lcp = ""

        for i in range(length):  # 短い文字列の長さだけループを回す
            if str1[i] != str2[i]:
                break
            lcp += str1[i]

        return lcp
# @lc code=end


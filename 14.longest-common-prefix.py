#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
'''
○実装方針

★longestCommonPrefixについて
1.初期状態のlcpはstrs[0]とする
2. strsの先頭 ~ strsの最後までの各文字列strに対し以下の行為を行う
    2-1.__getLCPByTwoStrsを呼ぶ
3.lcpを返却

★__getLCPByTwoStrsについて
1.引数で得たstr1とstr2に対し以下の操作を行う
2.それぞれ先頭から一文字(char)ずつ確認する
    2-1.異なる場合は終了
    2-2.同じ場合はlcpにcharを追加する
3.lcpを返却
'''
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        lcp = strs[0]
        for str in strs[1:]:
            lcp = self.__getLCPByTwoStrs(lcp, str)
            if lcp == '':
                break
        
        return lcp
        
    def __getLCPByTwoStrs(self, str1:  str, str2: str) -> str:
        lcp = ""
        
        for c1, c2 in zip(str1, str2):
            if c1 != c2:
                break
            lcp += c1
        return lcp
# @lc code=end


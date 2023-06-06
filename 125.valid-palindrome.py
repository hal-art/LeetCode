#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start

'''
★実装方針

●isPalindrome
1.s = convertStr()
2.sの先頭と末尾からそれぞれの文字が同一かどうかチェック
    2-1.異なる場合
        2-1-1.falseを返却して終了
3.この段階まで来たらpalindromeであることが確定する為true返却して終了

●convertStr
1.返却用の空文字列(converted_str)を用意
2.forを使ってstrの各文字(char)を探索する
    2-1.charが文字or数字ではない場合
        2-1-1.スキップ
    2-2.coverted_strにcharを追加
3.converted_strを返却して終了
'''
class Solution:
    def __convertStr(self, src: str) -> str:
        converted_str = []
        for char in src:
            if char.isalnum():
                converted_str.append(char.lower())
        return ''.join(converted_str)
    
    def isPalindrome(self, s: str) -> bool:
        s = self.__convertStr(s)
        is_palindrome = True
        start_index = 0
        end_index = len(s) - 1
        
        while start_index < end_index:
            if s[start_index] != s[end_index]:
                is_palindrome = False
                break
            
            start_index += 1
            end_index -= 1
            
        return is_palindrome

#obj = Solution()
#obj.isPalindrome("race a car")
# @lc code=end
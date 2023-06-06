#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start

'''
★実装方針

●isPalindrome
1.sの先頭及び最後から中央に向かって以下処理を実施
    1-1.先頭文字(left_char)が文字・数字では無い場合
        1-1-1.先頭文字インデックス(left_index)を増やしスキップ
    
    1-2.末尾文字(right_char)が文字・数字では無い場合
        1-2-1.末尾文字インデックス(right_index)を増やしスキップ
    
    1-3.left_char及びright_charを小文字に変換(lowered_left_char / lowered_right_char)
    1-4.lowered_left_charとlowered_right_charを比較
        1-4-1.異なる場合はis_palindromeをfalseにしてbreak
        1-4-2.同一の場合はleft_index及びright_indexを1増減させ次へ移行
2.is_palindromeを返却して終了
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        is_palindrome = True
        left_index = 0
        right_index = len(s) - 1
        
        while left_index < right_index:
            if not s[left_index].isalnum():
                left_index += 1
                continue
            
            if not s[right_index].isalnum():
                right_index -= 1
                continue
            
            lowered_left_char = s[left_index].lower()
            lowered_right_char = s[right_index].lower()
            
            if lowered_left_char != lowered_right_char:
                is_palindrome = False
                break
            
            left_index += 1
            right_index -= 1
            
        return is_palindrome

#obj = Solution()
#obj.isPalindrome("race a car")
# @lc code=end
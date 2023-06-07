#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
'''
★問題の整理
ローマ数字をアラビア数字に変換する
ローマ数字とアラビア数字の紐付けは以下の通り。
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

ただ、I, X, Cについてはその限りではない。
-I-
    IV = 4
    IX = 9

-X-
    XL = 40
    XC = 90
    
-C-
    CD = 400
    CM = 900

★実装方針
1.sの各文字(si)を見ていく
2.siが、I / X / Cに該当する場合
    2-1.{si} + {si+1}も確認して数字に変換
    2-2.次の文字は確認しないようにする
    2-3.continue
3.siが該当しない場合は値に変換して次
'''
class Solution:
    romans_2_arabic_except_list = [ "I", "X", "C"]
    romans_2_arabic_dict = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
        "IV" : 4,
        "IX" : 9,
        "XL" : 40,
        "XC" : 90,
        "CD" : 400,
        "CM" : 900
    }
    
    def romanToInt(self, s: str) -> int:
        value = 0
        is_next_skip = False
        for i, char in enumerate(s):
            if is_next_skip:
                is_next_skip = False
                continue
            
            if char in self.romans_2_arabic_except_list and i+1 < len(s):
                except_char = char + s[i+1]
                if except_char in self.romans_2_arabic_dict:
                    value += self.romans_2_arabic_dict[except_char]
                    is_next_skip = True
                else:
                    value += self.romans_2_arabic_dict[char]
            else:
                value += self.romans_2_arabic_dict[char]
                
        return value
    
#obj = Solution()
#obj.romanToInt("MCMXCIV")
# @lc code=end

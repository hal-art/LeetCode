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

↓アルゴリズム改善後↓
ローマ数字は左側から大きい数字順に並ぶという特性がある。
そのため、もし現在の数字{si}よりも次の数字{si+1}の方が大きい場合は徐算をすればいい
'''
class Solution:
    char_to_int = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
    }
    
    def romanToInt(self, s: str) -> int:
        current_char_value = 0
        next_char_value = 0
        value = 0
        
        for i, c in enumerate(s):
            current_char_value = self.char_to_int[c]
            next_char_value = self.__get_next_char_value(s, i+1)
            
            if current_char_value < next_char_value:
                value -= current_char_value
            else:
                value += current_char_value
        
        return value
    
    def __get_next_char_value(self, src: str, next_index: int) -> int:
        if next_index >= len(src):
            return 0
        
        c = src[next_index]
        return self.char_to_int[c]
# @lc code=end

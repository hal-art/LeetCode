#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
import math

'''
★アルゴリズム方針

num ... numsの各要素

1. numとtargetの補数を計算する
2. 次のnumに移行する前に計算した補数が、過去に登録されているかどうか確認する
    2-1. 登録されている場合は、補数に対するインデックスと現在のインデックスを返却
    2-2. 登録されてない場合、ハッシュマップに登録して手順1に戻る
'''
class Solution:
    def twoSum(self, nums, target: int):
        complement_map = {}
        
        for i, num in enumerate(nums):
            #1
            complement = target - num
            
            #2
            if(complement in complement_map):
                #2-1
                return [complement_map[complement], i]
            else:
                #2-2
                complement_map[num] = i
# @lc code=end
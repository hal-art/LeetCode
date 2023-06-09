#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
'''
○実装方針
preorder-traversal(前序走査)のためstackを用いてdfsベースにて走査する

1.rootノードをstackにpushする
2.stackの中身が存在する間以下の操作を行う
    2-1.stackの先頭を取り出し現在のノード(currentNode)を取り出す。
    2-2.ノードを訪問したため、出力リスト(outList)にvalを追加する
    
    2-3.currentNodeの左子ノード(leftNode)が存在する場合
        2-3-1.stackにleftNodeを追加する
    2-4.currentNodeの右子ノード(rightNode)が存在する場合
        2-4-1.stackにrightNodeを追加する
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, tree: TreeNode):
        if tree is None:
            return []
        
        outList: list[int] = []
        stack: list[TreeNode] = [tree]
        
        while stack:
            currentNode = stack.pop()
            outList.append(currentNode.val)
            
            if not currentNode.right is None:
                stack.append(currentNode.right)
                
            if not currentNode.left is None:
                stack.append(currentNode.left)
        return outList
# @lc code=end


#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
'''
○実装方針
1.rootノードをenqueする
2.以下を i(=1) < len(root)の間行う
    2-1.dequeして現在のノード情報を取り出す
    2-1.root[i]があるか確認する
        2-1-1.ある場合はNode(root[i])をし左子ノードを作成する
        2-1-2.enqueを行い、左子ノードを検査対象に含める
        2-1-3.i++
        
    2-2.root[i+1]があるか確認する
        2-2-1.ある場合はNode(root[i+1])をし右子ノードを作成する
        2-2-2.enqueを行い、右子ノードを検査対象に含める
        2-2-3.i++
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
#obj = Solution()
#obj.preorderTraversal([1,None,2,3])
# @lc code=end


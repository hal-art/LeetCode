#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
'''
●訪問済みフラグがTrueに設定される
    →「そのノードとその子ノード全てがスタックにpushされた」
●出力リストに追加される
    →「そのノードの全ての子ノードが出力リストに追加された」
'''
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        stack:list[TreeNode] = [[root, False]]
        outList: list[int] = []
        
        currentNode: TreeNode = None
        visited: bool = False
        while stack:
            currentNode, visited = stack.pop()
            if visited == False:
                stack.append([currentNode, True])
                if currentNode.right:
                    stack.append([currentNode.right, False])
                if currentNode.left:
                    stack.append([currentNode.left, False])
            else:
                outList.append(currentNode.val)
            
        return outList
# @lc code=end

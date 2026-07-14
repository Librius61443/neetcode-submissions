# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)
        
    
    def dfs(self, node: TreeNode, maxi: int) -> int:
        cur = 0
        if node is None: return 0
        if node.val >= maxi:
            cur = 1
            maxi = node.val

        left = self.dfs(node.left, maxi)
        right = self.dfs(node.right, maxi)

        return cur + left + right
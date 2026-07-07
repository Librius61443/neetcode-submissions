# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.dfs(root, p, q)
    
    def dfs(self, cur: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if cur == None:
            return None
        
        if cur.val == p.val or cur.val == q.val:
            return cur
        
        right = self.dfs(cur.right, p, q)
        left = self.dfs(cur.left, p, q)

        if right and left:
            return cur
        
        return right or left
        

        

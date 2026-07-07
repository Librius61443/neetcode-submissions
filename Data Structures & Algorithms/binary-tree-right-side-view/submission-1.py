# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        que = deque()
        que.append(root)

        while que:
            n = len(que)
            if que[-1]:
                res.append(que[-1].val)
            for i in range(n):
                cur = que.popleft()
                if cur:
                    if cur.left:
                        que.append(cur.left)
                    if cur.right:
                        que.append(cur.right)
            
        
        return res
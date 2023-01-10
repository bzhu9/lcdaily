# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def trav (p, q):
            if not p and not q:
                return True
            if p and q:
                if p.val != q.val:
                    return False
                return trav(p.left, q.left) and trav(p.right, q.right)
            return False
        return trav(p, q)

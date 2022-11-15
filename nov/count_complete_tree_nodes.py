# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def lheight(node):
    return 1 if not node else lheight(node.left) + 1
def rheight(node):
    return 1 if not node else rheight(node.right) + 1
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if lheight(root.left) == rheight(root.right):
            return 2**lheight(root.left) - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

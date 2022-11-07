# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        last = root
        while root != None:
            if root.left:
                last = root
                root = root.left
            elif root.right:
                pass
            else:
                l.append(root.val)

            root = None
            root = last

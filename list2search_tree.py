# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.makeBST(nums, 0, len(nums) - 1)
    
    def makeBST(self, nums, l, r):
        if l > r:
            return None
        mid = (r + l) // 2
        root = TreeNode(nums[mid])
        leftTree = self.makeBST(nums, l, mid - 1)
        rightTree = self.makeBST(nums, mid + 1, r)
        root.left = leftTree
        root.right = rightTree
        return root

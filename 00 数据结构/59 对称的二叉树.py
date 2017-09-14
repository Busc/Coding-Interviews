# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # wri2te code here
        return self.isSymBT(pRoot, pRoot)

    def isSymBT(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return self.isSymBT(root1.left, root2.right) and self.isSymBT(root1.right, root2.left)
    
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        lDepth = self.TreeDepth(pRoot.left)
        rDepth = self.TreeDepth(pRoot.right)
        return max(lDepth, rDepth) + 1
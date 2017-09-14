# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isBalanced(self, pRoot):
        # flag:当前子树是否为平衡二叉树
        # depth:当前遍历的节点的深度（它到叶节点的路径长度）
        if not pRoot:
            return True, 0
        l_flag, l_depth = self.isBalanced(pRoot.left)
        r_flag, r_depth = self.isBalanced(pRoot.right)
        if l_flag and r_flag:
            if abs(l_depth - r_depth) <= 1:
                return True, max(l_depth, r_depth)+1
        return False, max(l_depth, r_depth)+1

    def IsBalanced_Solution(self, pRoot):
        # write code here
        return self.isBalanced(pRoot)[0]

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def NodeList(self, pRootOfTree):
        if not pRootOfTree:
            return []
        return self.NodeList(pRootOfTree.left)+[pRootOfTree]+self.NodeList(pRootOfTree.right)

    def Convert(self, pRootOfTree):
        # write code here
        res = self.NodeList(pRootOfTree)
        lenR = len(res)
        if lenR == 0:
            return None
        elif lenR == 1:
            return res[0]
        else:
            res[0].left = None
            res[0].right = res[1]
            res[-1].left = res[-2]
            res[-1].right = None
            for i in range(1, len(res)-1):
                res[i].left = res[i-1]
                res[i].right = res[i+1]
            return res[0]
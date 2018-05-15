# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        # 该节点有右子树
        if pNode.right:
            leftest = pNode.right
            # 寻找右子树中的最左节点
            while leftest.left:
                leftest = leftest.left
            return leftest
        # 该节点无右子树
        while pNode.next:
            # 一直向上寻找
            dad = pNode.next
            # 该节点是父节点的左节点
            if dad.left == pNode:
                return dad
            pNode = dad

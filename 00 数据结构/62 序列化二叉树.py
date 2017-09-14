# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:

    def __init__(self):
        self.flag = -1

    def Serialize(self, root):
        # write code here
        if not root:
            return '$'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        # 仿照流读取
        self.flag += 1
        ss = s.split(',')
        if self.flag >= len(ss):
            return None

        if ss[self.flag] != '$':
            root = TreeNode(int(ss[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
            return root
        else:
            return None
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        # 时间复杂度O（两链长之和-公共链长）
        p1 = pHead1
        p2 = pHead2
        while p1 != p2:
            p1 = p1.next if p1 != None else pHead2
            p2 = p2.next if p2 != None else pHead1
        return p1
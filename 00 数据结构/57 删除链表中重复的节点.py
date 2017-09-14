# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        pre = ListNode(-1)
        curr = pHead
        res = pre
        flag = False
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
                flag = True
            if flag:
                curr = curr.next
                flag = False
            else:
                pre.next = curr
                pre = pre.next
                curr = curr.next
            if not curr:
                pre.next = None
        return res.next
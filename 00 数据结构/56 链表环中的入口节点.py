# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead or not pHead.next or not pHead.next.next:
            return None
        # 快慢指针判断链表是否有环
        low = pHead.next
        fast = pHead.next.next
        while low!=fast:
            # 无欢
            if not fast.next or not fast.next.next:
                return None
            low = low.next
            fast = fast.next.next
        # 快慢指针已相遇，已找到环中的节点
        fast = pHead
        while low!=fast:
            low = low.next
            fast = fast.next
        return fast
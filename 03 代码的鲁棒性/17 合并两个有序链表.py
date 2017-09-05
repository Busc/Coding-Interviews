# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def MergeRec(self, pHead1, pHead2):
        if (not pHead1) or (not pHead2):
            return pHead1 or pHead2
        if pHead1.val <= pHead2.val:
            pHead = pHead1
            pHead.next = self.Merge(pHead1.next, pHead2)
        else:
            pHead = pHead2
            pHead.next = self.Merge(pHead1, pHead2.next)
        return pHead

    def MergeLoop(self, pHead1, pHead2):
        # write code here
        # create 'pHead' as a ListNode
        pHead = ListNode(None)
        mergeHead = pHead
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                pHead.next = pHead1
                pHead1 = pHead1.next
            else:
                pHead.next = pHead2
                pHead2 = pHead2.next
            pHead = pHead.next
        pHead.next = pHead1 or pHead2
        #if pHead1:
        #    pHead.next = pHead1
        #if pHead2:
        #    pHead.next = pHead2
        return mergeHead.next

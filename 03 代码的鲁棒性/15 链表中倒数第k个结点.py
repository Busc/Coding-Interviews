# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if (not head) or (k == 0):
            return None
        ahead = head
        for i in range(k-1):
            if ahead.next:
                ahead = ahead.next
            else:
                return None
        behind = head
        while ahead.next:
            ahead = ahead.next
            behind = behind.next
        return behind
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        stack = []
        invResult = []
        while listNode:
            stack.append(listNode.val)
            listNode = listNode.next
        #return stack[::-1]
        while stack:
            invResult.append(stack.pop())
        return invResult
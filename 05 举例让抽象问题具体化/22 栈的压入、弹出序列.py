"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。

假设压入栈的所有数字均不相等。
"""

# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or not popV or len(pushV) != len(popV):
            return False
        stack = []
        isOrder = True
        for popInt in popV:
            if popInt in pushV:
                popInd = pushV.index(popInt)
                stack += pushV[0:popInd]
                pushV = pushV[popInd+1:]
            elif (popInt not in pushV and popInt not in stack) or popInt != stack.pop():
                isOrder = False
                break
        return isOrder